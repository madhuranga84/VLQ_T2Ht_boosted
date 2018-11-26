from __future__ import division

import ROOT as root
from ROOT import  TFile
import numpy as np
import sys
from array import array
from tagdefs import *
#import matplotlib.pyplot as plt


root.gStyle.SetOptStat(0)


# import the file to read

ff = TFile.Open("/afs/cern.ch/user/m/mmadugod/work/VLQ_T2Ht_boosted/combined.root")

if ff.IsOpen():
    print ">>> \nfile opened successfully!"


# regions = {

#     "ljet2_pt_passed_0b_0t0H" : 'A',
#     "ljet2_pt_passed_0b_1t0H" : 'B',
#     "ljet2_pt_passed_0b_0t1H" : 'C',
#     "ljet1_pt_passed_0b_1t1H" : 'D',

#     "ljet1_pt_passed_3b_0t0H" : 'M',
#     "ljet1_pt_passed_3b_1t0H" : 'N',
#     "ljet1_pt_passed_3b_0t1H" : 'O',
#     "ljet1_pt_passed_3b_1t1H" : 'S',
# }



jet = "ljet2"
dis = "pt"


hists = [

    jet+"_"+dis+"_passed_0b_0t0H", jet+"_"+dis+"_passed_0b_1t0H", jet+"_"+dis+"_passed_0b_0t1H", jet+"_"+dis+"_passed_0b_1t1H",
    jet+"_"+dis+"_passed_1b_0t0H", jet+"_"+dis+"_passed_1b_1t0H", jet+"_"+dis+"_passed_1b_0t1H", jet+"_"+dis+"_passed_1b_1t1H",
    jet+"_"+dis+"_passed_2b_0t0H", jet+"_"+dis+"_passed_2b_1t0H", jet+"_"+dis+"_passed_2b_0t1H", jet+"_"+dis+"_passed_2b_1t1H",
    jet+"_"+dis+"_passed_3b_0t0H", jet+"_"+dis+"_passed_3b_1t0H", jet+"_"+dis+"_passed_3b_0t1H", jet+"_"+dis+"_passed_3b_1t1H",
    ]


ha = ff.Get(hists[0])
inte_a = ha.Integral(0, ha.GetNbinsX()+1  )

hb = ff.Get(hists[1])
inte_b = hb.Integral(0, ha.GetNbinsX()+1  )

hc = ff.Get(hists[2])
inte_c = hc.Integral(0, ha.GetNbinsX()+1   )

hd = ff.Get(hists[3])
inte_d = hd.Integral(0, ha.GetNbinsX()+1   )



he = ff.Get(hists[4])
inte_e = he.Integral(0, ha.GetNbinsX()+1  )

hf = ff.Get(hists[5])
inte_f = hf.Integral(0, ha.GetNbinsX()+1  )

hg = ff.Get(hists[6])
inte_g = hg.Integral(0, ha.GetNbinsX()+1   )

hh = ff.Get(hists[7])
inte_h = hh.Integral(0, ha.GetNbinsX()+1   )



hi = ff.Get(hists[8])
inte_i = hi.Integral(0, ha.GetNbinsX()+1  )

hj = ff.Get(hists[9])
inte_j = hj.Integral(0, ha.GetNbinsX()+1  )

hk = ff.Get(hists[10])
inte_k = hk.Integral(0, ha.GetNbinsX()+1   )

hl = ff.Get(hists[11])
inte_l = hl.Integral(0, ha.GetNbinsX()+1   )



hm = ff.Get(hists[12])
inte_m = hm.Integral(0, ha.GetNbinsX()+1   )

hn = ff.Get(hists[13])
inte_n = hn.Integral(0, ha.GetNbinsX()+1   )

ho = ff.Get(hists[14])
inte_o = ho.Integral(0, ha.GetNbinsX()+1   )


n_est = (inte_b * inte_m) / (inte_a) 

o_est = (inte_c * inte_m) / (inte_a)

k_est = (inte_c * inte_i) / (inte_a)

j_est = (inte_b * inte_i) / (inte_a)

l_est = (inte_d * inte_i) / (inte_a) 

i_est = (inte_a * inte_j) / (inte_b)

h_est = (inte_d * inte_e) / (inte_a)

s_est = (inte_d * inte_o * inte_n * inte_a) / (inte_m * inte_b * inte_c)


# print "____________________________________\n"
# print "true value for region N: ", inte_n
# print "\n__________________________________\n"
# print "estimated value for region N: ", n_est
# print "\n__________________________________\n"
# print "____________________________________\n"
# print "true value for region O: ", inte_o
# print "\n__________________________________\n"
# print "estimated value for region O: ", o_est
# print "\n__________________________________\n"
# print "____________________________________\n"
# print "true value for region K: ", inte_k
# print "\n__________________________________\n"
# print "estimated value for region K: ", k_est
# print "\n__________________________________\n"
# print "____________________________________\n"
# print "true value for region J: ", inte_j
# print "\n__________________________________\n"
# print "estimated value for region J: ", j_est
# print "\n__________________________________\n"
# print "____________________________________\n"
# print "true value for region L: ", inte_l
# print "\n__________________________________\n"
# print "estimated value for region L: ", l_est
# print "\n__________________________________\n"
# print "____________________________________\n"
# print "true value for region I: ", inte_i
# print "\n__________________________________\n"
# print "estimated value for region I: ", i_est
# print "\n__________________________________\n"
# print "____________________________________\n"
# print "true value for region H: ", inte_h
# print "\n__________________________________\n"
# print "estimated value for region H: ", h_est
# print "\n__________________________________\n"

# print "estimated value for region S: ", s_est
# print "\n__________________________________\n"


# bin by bin calculations


val = []
err = []
w = 1
for ii in xrange(0, ha.GetNbinsX()+1 ):

    try:
        s = ( hd.GetBinContent(ii) * ho.GetBinContent(ii) * hn.GetBinContent(ii) * ha.GetBinContent(ii) ) / (hc.GetBinContent(ii) * hm.GetBinContent(ii) * hb.GetBinContent(ii))

        serr = np.sqrt( ( (s/hd.GetBinContent(ii)) * (np.sqrt(hd.GetBinContent(ii) + 1)) )**2 + 
                        ( (s/ho.GetBinContent(ii)) * (np.sqrt(ho.GetBinContent(ii) + 1)) )**2 + 
                        ( (s/hn.GetBinContent(ii)) * (np.sqrt(hn.GetBinContent(ii) + 1)) )**2 + 
                        ( (s/ha.GetBinContent(ii)) * (np.sqrt(ha.GetBinContent(ii) + 1)) )**2 + 
                        ( (s/hc.GetBinContent(ii)) * (np.sqrt(hc.GetBinContent(ii) + 1)) )**2 + 
                        ( (s/hm.GetBinContent(ii)) * (np.sqrt(hm.GetBinContent(ii) + 1)) )**2 + 
                        ( (s/hb.GetBinContent(ii)) * (np.sqrt(hb.GetBinContent(ii) + 1)) )**2 
                        )

    except ZeroDivisionError:
       s = -1 
       serr = -1

    val.append(s)
    err.append(serr)



cval = []
bval = []
mval = []
dval = []
oval = []
nval = []
aval = []
for ii in xrange(0, ha.GetNbinsX()+1 ):
    
    
    c = hc.GetBinContent(ii) 
    b = hb.GetBinContent(ii)
    m = hm.GetBinContent(ii)
    d = hd.GetBinContent(ii)
    o = ho.GetBinContent(ii) 
    n = hn.GetBinContent(ii)
    a = ha.GetBinContent(ii)
    
    cval.append(c)
    bval.append(b)
    mval.append(m)
    dval.append(d)
    oval.append(o)
    nval.append(n)
    aval.append(a)
    
    
print "values in region C: ", cval
print "values in region B: ", bval
print "values in region M: ", mval
print ""
print "values in region D: ", dval
print "values in region O: ", oval
print "values in region N: ", nval
print "values in region A: ", aval

print "bin-by-bin values: ", val
# print "length of val: ", len(val)

# print ""

# print "bin-by-bin errors: ", err
# print "length of err: ", len(err)


#print ha.GetNbinsX(), ha.GetBinLowEdge(1), ha.GetBinLowEdge( ha.GetNbinsX() +1 )
 

histo = root.TH1D("","Bin-by-bin estimation for region: S",ha.GetNbinsX(), ha.GetBinLowEdge(1), ha.GetBinLowEdge( ha.GetNbinsX() +1 ) )
# histo = root.TH1D("","Bin-by-bin distribution for region: O",ha.GetNbinsX(), ha.GetBinLowEdge(1), ha.GetBinLowEdge( ha.GetNbinsX() +1 ) )

if jet == "ljet1" and dis == "m":
    histo.GetXaxis().SetTitle("1st Large-R jet mass [GeV]")
elif jet == "ljet1" and dis == "pt":
    histo.GetXaxis().SetTitle("1st Large-R jet p_{T} [GeV]")
elif jet == "ljet2" and dis == "m":
    histo.GetXaxis().SetTitle("2nd Large-R jet mass [GeV]")
elif jet == "ljet2" and dis == "pt":
    histo.GetXaxis().SetTitle("2nd Large-R jet p_{T} [GeV]")



histo.GetYaxis().SetTitle("Events/Bin")
histo.SetLineWidth(1)

histo.SetLineColor(root.kRed)
histo.SetFillColorAlpha(root.kRed, 0.26)

# histo.SetLineColor(root.kBlue)
# histo.SetFillColorAlpha(root.kBlue, 0.26)

for jj in xrange(0, len(val)):
    histo.SetBinContent(jj, val[jj])

for kk in xrange(0, len(err)):
    histo.SetBinError(kk, err[kk])


c = root.TCanvas("c", "c", 800, 600)
c.SetGrid(1,1)
if dis == 'pt':
    c.SetLogy(1)
    c.SetGrid(0,0)
else:
    c.SetLogy(0)
c.cd()
histo.Draw('HIST E1')
c.Update()
c.SaveAs('plots/'+jet+'_'+dis+'_s.pdf')


# a = np.asarray(val)
# f = plt.figure()
# plt.hist(a, bins=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
# plt.ylim(0,6)
# plt.title("Bin-by-bin signal estimation")
# plt.xlabel("1st LArge-R jet p_{T}")
# plt.ylabel("Events/Bin")
# plt.yscale('linear')
# plt.show()
# f.savefig("new.pdf")


# end of the code

#inte_a = ha.Integral(0, ha.GetNbinsX() + 1 )
