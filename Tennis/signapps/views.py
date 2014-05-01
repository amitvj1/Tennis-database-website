import psycopg2
import sys
import os
from django.shortcuts import render,render_to_response,RequestContext

# Create your views here.

from .forms import SignUpForm
from .forms import PlayerForm
from .forms import H2HForm
from .forms import RecentResultForm
from .forms import SearchResultForm
from .forms import IndividualRankForm
from .forms import PlayerRankForm
from .forms import CompleteRankingForm
def completeRanking(request):
    form = CompleteRankingForm(request.POST or None)
    con = None

    try:
         
        con = psycopg2.connect(database='tennis1', user='amit')     
        cur = con.cursor()
        #print "select * from c_stats where p_name = "+(var)
        #cur.execute(request.PO ST.get("sqlQuery", ""))
        #cur.execute("select * from c_stats where p_name =  'Rafael Nadal'")#\'+var\'
        cur.execute("select * from ranking_t")#select * from c_stats where p_name =  request.POST.get("sqlQuery", "")
        f = open('result.html','w+')
        f.write('<table> <tbody>')
        rows = cur.fetchall();
        for row in rows:
            f.write( '<tr>')
            for column in row:
                f.write( '<td>')
                f.write(str(column))
                f.write( '</td>')
            f.write( '</tr>')
        f.write( '</tbody></table>')
        f.close()    
    
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)
        
        
    finally:
        
        if con:
            con.close()
        #if f:
        
    #save_it.save()
    return render_to_response("result.html",locals(),context_instance=RequestContext(request))
    #return recentResult("result.html")

def playerByRank(request):
    form = PlayerRankForm(request.POST or None)
    if form.is_valid():
        #save_it = form.save(commit=False)
        
        con = None

        try:
             
            con = psycopg2.connect(database='tennis1', user='amit')     
            cur = con.cursor()
            var = request.POST.get("player_rank", "")
            #print "select * from c_stats where p_name = "+(var)
            #cur.execute(request.PO ST.get("sqlQuery", ""))
            #cur.execute("select * from c_stats where p_name =  'Rafael Nadal'")#\'+var\'
            cur.execute("select * from ranking_t where rank = "+var)#select * from c_stats where p_name =  request.POST.get("sqlQuery", "")
            f = open('result.html','w+')
            f.write('<table> <tbody>')
            rows = cur.fetchall();
            for row in rows:
                f.write( '<tr>')
                for column in row:
                    f.write( '<td>')
                    f.write(str(column))
                    f.write( '</td>')
                f.write( '</tr>')
            f.write( '</tbody></table>')
            f.close()    
        
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e    
            sys.exit(1)
            
            
        finally:
            
            if con:
                con.close()
            #if f:
            
        #save_it.save()
	return render_to_response("result.html",locals(),context_instance=RequestContext(request))

    return render_to_response("playerByRank.html",locals(),context_instance=RequestContext(request))
def individualRank(request):
    form = IndividualRankForm(request.POST or None)
    if form.is_valid():
        #save_it = form.save(commit=False)
        
        con = None

        try:
             
            con = psycopg2.connect(database='tennis1', user='amit')     
            cur = con.cursor()
            var = request.POST.get("player_name", "")
            #print "select * from c_stats where p_name = "+(var)
            #cur.execute(request.PO ST.get("sqlQuery", ""))
            #cur.execute("select * from c_stats where p_name =  'Rafael Nadal'")#\'+var\'
            cur.execute("select * from ranking_t where p_name = "+"'"+var+"'")#select * from c_stats where p_name =  request.POST.get("sqlQuery", "")
            f = open('result.html','w+')
            f.write('<table> <tbody>')
            rows = cur.fetchall();
            for row in rows:
                f.write( '<tr>')
                for column in row:
                    f.write( '<td>')
                    f.write(str(column))
                    f.write( '</td>')
                f.write( '</tr>')
            f.write( '</tbody></table>')
            f.close()    
        
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e    
            sys.exit(1)
            
            
        finally:
            
            if con:
                con.close()
            #if f:
            
        #save_it.save()
	return render_to_response("result.html",locals(),context_instance=RequestContext(request))

    return render_to_response("individualRank.html",locals(),context_instance=RequestContext(request))
def searchResult(request):
    form = SearchResultForm(request.POST or None)
    if form.is_valid():
        #save_it = form.save(commit=False)
        
        con = None

        try:
             
            con = psycopg2.connect(database='tennis1', user='amit')     
            cur = con.cursor()
            var1 = request.POST.get("Player_Name", "")
            var2 = request.POST.get("Tournament_Name", "")
            var3 = request.POST.get("year", "")
            #print "select * from c_stats where p_name = "+(var)
            #cur.execute(request.PO ST.get("sqlQuery", ""))
            #cur.execute("select * from c_stats where p_name =  'Rafael Nadal'")#\'+var\'
            cur.execute("select * from tournament_g where t_name = "+"'"+var2+"'"+" and year = "+"'"+var3+"'"+" and p_name = "+"'"+var1+"'")#select * from c_stats where p_name =  request.POST.get("sqlQuery", "")
            f = open('result.html','w+')
            f.write('<table> <tbody>')
            rows = cur.fetchall();
            for row in rows:
                f.write( '<tr>')
                for column in row:
                    f.write( '<td>')
                    f.write(str(column))
                    f.write( '</td>')
                f.write( '</tr>')
            f.write( '</tbody></table>')
            f.close()    
        
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e    
            sys.exit(1)
            
            
        finally:
            
            if con:
                con.close()
            #if f:
            
        #save_it.save()
	return render_to_response("result.html",locals(),context_instance=RequestContext(request))

    return render_to_response("searchResult.html",locals(),context_instance=RequestContext(request))
def recentResult(request):
    form = RecentResultForm(request.POST or None)
    if form.is_valid():
        #save_it = form.save(commit=False)
        
        con = None

        try:
             
            con = psycopg2.connect(database='tennis1', user='amit')     
            cur = con.cursor()
            var1 = request.POST.get("Tournament_Name", "")
            var2 = request.POST.get("year", "")
            #print "select * from c_stats where p_name = "+(var)
            #cur.execute(request.PO ST.get("sqlQuery", ""))
            #cur.execute("select * from c_stats where p_name =  'Rafael Nadal'")#\'+var\'
            cur.execute("select * from tournament_g where t_name = "+"'"+var1+"'"+" and year = "+"'"+var2+"'")#select * from c_stats where p_name =  request.POST.get("sqlQuery", "")
            f = open('result.html','w+')
            f.write('<table> <tbody>')
            rows = cur.fetchall();
            for row in rows:
                f.write( '<tr>')
                for column in row:
                    f.write( '<td>')
                    f.write(str(column))
                    f.write( '</td>')
                f.write( '</tr>')
            f.write( '</tbody></table>')
            f.close()    
        
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e    
            sys.exit(1)
            
            
        finally:
            
            if con:
                con.close()
            #if f:
            
        #save_it.save()
	return render_to_response("result.html",locals(),context_instance=RequestContext(request))

    return render_to_response("recentResult.html",locals(),context_instance=RequestContext(request))
def h2h(request):
    form = H2HForm(request.POST or None)
    if form.is_valid():
        #save_it = form.save(commit=False)
        
        con = None

        try:
             
            con = psycopg2.connect(database='tennis1', user='amit')     
            cur = con.cursor()
            var1 = request.POST.get("player_1", "")
            var2 = request.POST.get("player_2", "")
            #print "select * from c_stats where p_name = "+(var)
            #cur.execute(request.PO ST.get("sqlQuery", ""))
            #cur.execute("select * from c_stats where p_name =  'Rafael Nadal'")#\'+var\'
            cur.execute("select * from h2h where p1_name = "+"'"+var1+"'"+" and p2_name = "+"'"+var2+"'")#select * from c_stats where p_name =  request.POST.get("sqlQuery", "")
            f = open('result.html','w+')
            f.write('<table> <tbody>')
            rows = cur.fetchall();
            for row in rows:
                f.write( '<tr>')
                for column in row:
                    f.write( '<td>')
                    f.write(str(column))
                    f.write( '</td>')
                f.write( '</tr>')
            f.write( '</tbody></table>')
            f.close()    
        
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e    
            sys.exit(1)
            
            
        finally:
            
            if con:
                con.close()
            #if f:
            
        #save_it.save()
	return render_to_response("result.html",locals(),context_instance=RequestContext(request))

    return render_to_response("h2h.html",locals(),context_instance=RequestContext(request))
def players(request):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        #save_it = form.save(commit=False)
        
        con = None

        try:
             
            con = psycopg2.connect(database='tennis1', user='amit')     
            cur = con.cursor()
            var = request.POST.get("search_player", "")
            #print "select * from c_stats where p_name = "+(var)
            #cur.execute(request.PO ST.get("sqlQuery", ""))
            #cur.execute("select * from c_stats where p_name =  'Rafael Nadal'")#\'+var\'
            if(var == 'Left-handed' or var == 'Right-handed'):
                cur.execute("select * from players where style_of_play = "+"'"+var+"'")
            elif(len(var) == 3):
                cur.execute("select * from players where Nationality = "+"'"+var+"'")
            else:
                cur.execute("select * from c_stats where p_name = "+"'"+var+"'")#select * from c_stats where p_name =  request.POST.get("sqlQuery", "")
            f = open('result.html','w+')
            f.write('<table> <tbody>')
            rows = cur.fetchall();
            for row in rows:
                f.write( '<tr>')
                for column in row:
                    f.write( '<td>')
                    f.write(str(column))
                    f.write( '</td>')
                f.write( '</tr>')
            f.write( '</tbody></table>')
            f.close()    
        
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e    
            sys.exit(1)
            
            
        finally:
            
            if con:
                con.close()
            #if f:
            
        #save_it.save()
	return render_to_response("result.html",locals(),context_instance=RequestContext(request))

    return render_to_response("page1.html",locals(),context_instance=RequestContext(request))
    
def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        #save_it = form.save(commit=False)
        
        con = None

        try:
             
            con = psycopg2.connect(database='tennis1', user='amit')     
            cur = con.cursor()
            var = request.POST.get("sqlQuery", "")
            #print "select * from c_stats where p_name = "+(var)
            #cur.execute(request.POST.get("sqlQuery", ""))
            #cur.execute("select * from c_stats where p_name =  'Rafael Nadal'")#\'+var\'
            if(var == 'Left-handed' or var == 'Right-handed'):
                cur.execute("select * from players where style_of_play = "+"'"+var+"'")
            elif(len(var) == 3):
                cur.execute("select * from players where Nationality = "+"'"+var+"'")
            else:
                cur.execute("select * from players where p_name = "+"'"+var+"'")#select * from c_stats where p_name =  request.POST.get("sqlQuery", "")
            f = open('result.html','w+')
            f.write('<table> <tbody>')
            rows = cur.fetchall();
            for row in rows:
                f.write( '<tr>')
                for column in row:
                    f.write( '<td>')
                    f.write(str(column))
                    f.write( '</td>')
                f.write( '</tr>')
            f.write( '</tbody></table>')
            f.close()    
        
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e    
            sys.exit(1)
            
            
        finally:
            
            if con:
                con.close()
            #if f:
            
        #save_it.save()
	return render_to_response("result.html",locals(),context_instance=RequestContext(request))
    
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))



