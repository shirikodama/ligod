from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
import xmltodict, json
import lxml.etree
from datetime import datetime
from .models import Gwave

def gwave_index(request):
    gwaves = Gwave.objects.order_by('-id')
    template = loader.get_template('gwaves/index.html')
    for gwave in gwaves:        
        gwave.r_date = datetime.fromtimestamp(gwave.received_at).strftime('%Y-%m-%d %H:%M:%S')
        if gwave.exploded_at == 0:
            gwave.x_date = gwave.r_date
        else:
            gwave.x_date = datetime.fromtimestamp(gwave.exploded_at).strftime('%Y-%m-%d %H:%M:%S')
        if gwave.alerttype == '':
            gwave.alerttype = 'Unknown'
    context = {
        'gwaves': gwaves,
    } 
    return HttpResponse(template.render(context, request))


def gwave_view(request, gwave_id):
    print("@view")
    gwave = Gwave.objects.get(pk=gwave_id)
    template = loader.get_template('gwaves/show.html')
    dict = xmltodict.parse(gwave.msg)
    boom_time = dict['voe:VOEvent']['WhereWhen']['ObsDataLocation']["ObservationLocation"]['AstroCoords']['Time']['TimeInstant']['ISOTime']
    root = lxml.etree.fromstring(gwave.msg)    
    params = {elem.attrib['name']:
              elem.attrib['value']
              for elem in root.iterfind('.//Param')}
    if 'BNS' in params:    
        boom_max = float(params['BNS'])
        boom_type = 'Binary Neutron Stars'
        if float(params['BBH']) > boom_max:
            boom_max = float(params['BBH'])
            boom_type = 'Blockhole-Blackhole'
        elif float(params['NSBH']) > boom_max:
            boom_max = float(params['NSBH'])
            boom_type = 'Neutron Star-Blackhole'
        elif float(params['Terrestrial']) > boom_max:
            boom_max = float(params['Terrestrial'])
            boom_type = 'Terrestrial'
    else:
        boom_type = ''
        boom_max = 0
    boom_max *= 100.0
    context = {
        'gwave': gwave,
        'json': json.dumps(dict, indent=2, sort_keys=True),
        'params':params,
        'boom_type': boom_type,
        'boom_max': int(boom_max*100)/100.0,
        'boom_time': boom_time,
    } 
    return HttpResponse(template.render(context, request))

# placeholder as new is done by ligod

def gwave_new(request):
    print("@new")    
    form = GwaveForm(request.POST or None)
    if form.is_valid():
        form.save()    
    return redirect('gwave_index')

# placeholder as update doesn't make much sense for this incarnation

def gwave_edit(request, gwave_id):
    gwave = get_object_or_404(Gwave, pk=gwave_id)
    print("@edit")            
    form = GwaveForm(request.POST or None, instance=gwave)
    if form.is_valid():
        form.save()    
    return redirect('gwave_index')

def gwave_delete(request, gwave_id):
    gwave = get_object_or_404(Gwave, pk=gwave_id)
    print("@delete")    
    if request.method=='POST':    
        gwave.delete()
    return redirect('gwave_index')
