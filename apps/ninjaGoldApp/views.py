from django.shortcuts import render, HttpResponse, redirect
import random
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'energy' not in request.session:
        request.session['energy']=100
    if 'myActivities' not in request.session:
        request.session['myActivities']=[]
    if 'building' not in request.session:
        request.session['building']=None
    if request.session['energy']<0:
        request.session['energy']=0
        request.session['myActivities'].append(['You have died. START OVER'])
        request.session['color']='red'
    if request.session['energy']>100:
        request.session['energy']=100
    return render(request, "index.html")

def reset(request):
    request.method == "POST"
    del request.session['energy']
    del request.session['gold']
    del request.session['myActivities']
    del request.session['building']
    return redirect("/")

def process(request):
    request.method == "POST"
    request.session['winLose']=round(int(random.random()*100))
    if request.POST['building']=='farm':
        if request.session['energy']==0:
            request.session['myActivities'].append(['You have died. START OVER'])
            return redirect ('/')
        else:
            request.session['color']='green'
            request.session['building']='farm'
            request.session['farmMoney']=round(int(random.random()*15+5))
            request.session['gold']+=request.session['farmMoney']
            request.session['farmEnergy']=round(int(random.random()*15+5))
            request.session['energy']-=request.session['farmEnergy']
            request.session['myActivities'].append(['Earned '+str(request.session['farmMoney'])+' gold doing your cowperson business! Yawn but so productive! Lost '+str(request.session['farmEnergy'])+'% of your soul energy charge from back-breaking work'])
            return redirect ('/')
    elif request.POST['building']=='cave':
        if request.session['energy']==0:
            request.session['myActivities'].append(['You have died. START OVER'])
            return redirect ('/')
        else:
            request.session['color']='green'
            request.session['building']='cave'
            request.session['caveMoney']=round(int(random.random()*20+10))
            request.session['gold']+=request.session['caveMoney']
            request.session['caveEnergy']=round(int(random.random()*20+10))
            request.session['energy']-=request.session['caveEnergy']
            request.session['myActivities'].append(['Earned '+str(request.session['caveMoney'])+' gold mining hydrogen flouride. Your abs may be made of steel but your back is howling is pain. Lost '+str(request.session['caveEnergy'])+'% of your soul energy charge.'])
            return redirect ('/')
    elif request.POST['building']=='house' and request.session['energy'] is not 0:
        if request.session['energy']==0:
            request.session['myActivities'].append('You have died. START OVER')
            return redirect ('/')
        else:
            request.session['color']='green'
            request.session['building']='house'
            request.session['houseMoney']=round(int(random.random()*2))
            request.session['gold']+=request.session['houseMoney']
            request.session['houseEnergy']=round(int(random.random()*20))
            request.session['energy']+=request.session['houseEnergy']
            request.session['myActivities'].append(['Family gave you an allowance of '+str(request.session['houseMoney'])+' gold. You feel loved! Re-energized ' +str(request.session['houseEnergy'])+'% of your soul energy charge.'])
            return redirect ('/')
    else:
        if request.session['energy']==0:
            session['myActivities'].append(['You have died. START OVER'])
            return redirect ('/')
        else:
            request.session['building']='casino'
            request.session['casinoMoney']=round(int(random.random()*15+5))
            request.session['gold']+=request.session['casinoMoney']
            request.session['casinoEnergy']=round(int(random.random()*15+5))
            request.session['energy']-=request.session['casinoEnergy']
            if request.session['winLose']%2==0:
                request.session['color']='green'
                request.session['myActivities'].append('You lucky bug! Won '+str(request.session['casinoMoney'])+' gold but lost '+str(request.session['casinoEnergy'])+'% of your soul charge for the sin.')
                return redirect('/')
            else:
                request.session['color']='red'
                request.session['myActivities'].append('Oof! You were served with $'+str(request.session['casinoMoney'])+' gold but lost '+str(request.session['casinoEnergy'])+'% of your soul charge for the sin.')
                return redirect ('/')