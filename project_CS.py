import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import *
from PyQt5.Qt import QStandardItemModel, QStandardItem
import mexicoSoup
import csv

mexicoCovData = []

class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Courier New', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('PROJECT CODE SCRAPER')
        self.setGeometry(0,0, 2000, 1000)

        hbox = QHBoxLayout()
        # Canada Tree View
        treeView = QTreeView(self)
        treeView.setHeaderHidden(True)
        treeView.setFixedWidth(380)
        treeView.setFixedHeight(800)
   
        treeView.setStyleSheet('QTreeView {\
                          margin: left;\
                          background-color:lightgray;\
                          border-style: outset;\
                          border-width: 2px;\
                          border-corlor: beige;\
                          padding: 2px;\
                          }')

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()
      
        # Canada Data
        canada = StandardItem('Canada', 14, set_bold=True, color=QColor(255, 0, 0))

        nl = StandardItem('Newfoundland and Labrador', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(nl)
        case = StandardItem("cases: 256")
        death = StandardItem("deaths: 3")
        nl.appendRow(case)
        nl.appendRow(death)

        pe = StandardItem('Prince Edward Island', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(pe)
        case = StandardItem("cases: 26")
        death = StandardItem("deaths: 0")
        pe.appendRow(case)
        pe.appendRow(death)

        ns = StandardItem('Nova Scotia',set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(ns)
        case = StandardItem("cases: 827")
        death = StandardItem("deaths: 16")
        ns.appendRow(case)
        ns.appendRow(death)

        nb = StandardItem('New Brunswick', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(nb)
        case = StandardItem("cases: 118")
        death = StandardItem("deaths: 0")
        nb.appendRow(case)
        nb.appendRow(death)

        quebec = StandardItem('Quebec', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(quebec)
        case = StandardItem("cases: 21,838")
        death = StandardItem("deaths: 243")
        quebec.appendRow(case)
        quebec.appendRow(death)

        ontario = StandardItem('Ontario', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(ontario)
        case = StandardItem("cases: 12,879")
        death = StandardItem("deaths: 713")
        ontario.appendRow(case)
        ontario.appendRow(death)

        manitoba = StandardItem('Manitoba', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(manitoba)
        case = StandardItem("cases: 251")
        death = StandardItem("deaths: 6")
        manitoba.appendRow(case)
        manitoba.appendRow(death)

        saskatchewan = StandardItem('Saskatchewan', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(saskatchewan)
        case = StandardItem("cases: 331")
        death = StandardItem("deaths: 4")
        saskatchewan.appendRow(case)
        saskatchewan.appendRow(death)

        alberta = StandardItem('Alberta', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(alberta)
        case = StandardItem("cases: 3,720")
        death = StandardItem("deaths: 67")
        alberta.appendRow(case)
        alberta.appendRow(death)

        bc = StandardItem('Bristis Columbia', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(bc)
        case = StandardItem("cases: 1,824")
        death = StandardItem("deaths: 94")
        bc.appendRow(case)
        bc.appendRow(death)

        yukon = StandardItem('Yukon', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(yukon)
        case = StandardItem("cases: 11")
        death = StandardItem("deaths: 0")
        yukon.appendRow(case)
        yukon.appendRow(death)

        nt = StandardItem('Northwest Teritories', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(nt)
        case = StandardItem("cases: 5")
        death = StandardItem("deaths: 0")
        nt.appendRow(case)
        nt.appendRow(death)

        nunavut = StandardItem('Nunavut', set_bold=True, color=QColor(102, 51, 0))
        canada.appendRow(alberta)
        case = StandardItem("cases: 0")
        death = StandardItem("deaths: 0")
        nunavut.appendRow(case)
        nunavut.appendRow(death)

        rootNode.appendRow(canada)
        treeView.setModel(treeModel)

        # USA Tree View
        treeViewUS = QTreeView(self)
        treeViewUS.setHeaderHidden(True)
        treeViewUS.setFixedWidth(380)
        treeViewUS.setFixedHeight(800)
        
        treeViewUS.setStyleSheet('QTreeView {\
                          margin: left;\
                          background-color:lightgray;\
                          border-style: inset;\
                          border-width: 2px;\
                          border-corlor: beige;\
                          padding: 2px;\
                          }')

        treeModelUS = QStandardItemModel()
        rootNodeUS = treeModelUS.invisibleRootItem()

        # USA Data
        usa = StandardItem('USA', 14, set_bold=True, color=QColor(0, 0, 204))

        ny = StandardItem('NewYork', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ny)
        case = StandardItem("cases: 291,996")
        death = StandardItem("deaths: 22,585")
        ny.appendRow(case)
        ny.appendRow(death)

        nj = StandardItem('New Jersey', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nj)
        case = StandardItem("cases: 111,188")
        death = StandardItem("deaths: 6,044")
        nj.appendRow(case)
        nj.appendRow(death)

        ma = StandardItem('Massachusetts',set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ma)
        case = StandardItem("cases: 54,938")
        death = StandardItem("deaths: 2,899")
        ma.appendRow(case)
        ma.appendRow(death)

        il = StandardItem('Illinois', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(il)
        case = StandardItem("cases: 43,903")
        death = StandardItem("deaths: 1,933")
        il.appendRow(case)
        il.appendRow(death)

        ca = StandardItem('California', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ca)
        case = StandardItem("cases: 43,801")
        death = StandardItem("deaths: 1,724")
        ca.appendRow(case)
        ca.appendRow(death)

        pa = StandardItem('Pennsylvania', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(pa)
        case = StandardItem("cases: 43,255")
        death = StandardItem("deaths: 1,866")
        pa.appendRow(case)
        pa.appendRow(death)

        mi = StandardItem('Michigan', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(mi)
        case = StandardItem("cases: 38,113")
        death = StandardItem("deaths: 3,364")
        mi.appendRow(case)
        mi.appendRow(death)

        fl = StandardItem('Florida', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(fl)
        case = StandardItem("cases: 32,138")
        death = StandardItem("deaths: 1,088")
        fl.appendRow(case)
        fl.appendRow(death)

        la = StandardItem('Louisiana', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(la)
        case = StandardItem("cases: 27,068")
        death = StandardItem("deaths: 1,740")
        la.appendRow(case)
        la.appendRow(death)

        tx = StandardItem('Texas', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(tx)
        case = StandardItem("cases: 25,292")
        death = StandardItem("deaths: 661")
        tx.appendRow(case)
        tx.appendRow(death)

        ct = StandardItem('Connecticut', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ct)
        case = StandardItem("cases: 25,269")
        death = StandardItem("deaths: 1,924")
        ct.appendRow(case)
        ct.appendRow(death)

        ga = StandardItem('Georgia', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ga)
        case = StandardItem("cases: 23,773")
        death = StandardItem("deaths: 942")
        ga.appendRow(case)
        ga.appendRow(death)

        md = StandardItem('Maryland', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(md)
        case = StandardItem("cases: 19,487")
        death = StandardItem("deaths: 945")
        md.appendRow(case)
        md.appendRow(death)

        oh = StandardItem('Ohio', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(oh)
        case = StandardItem("cases: 16,325")
        death = StandardItem("deaths: 753")
        oh.appendRow(case)
        oh.appendRow(death)

        ind = StandardItem('Indiana', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ind)
        case = StandardItem("cases: 15,961")
        death = StandardItem("deaths: 844")
        ind.appendRow(case)
        ind.appendRow(death)

        va = StandardItem('Virginia', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(va)
        case = StandardItem("cases: 13,538")
        death = StandardItem("deaths: 460")
        va.appendRow(case)
        va.appendRow(death)

        wa = StandardItem('Washington', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(wa)
        case = StandardItem("cases: 13,521")
        death = StandardItem("deaths: 749")
        wa.appendRow(case)
        wa.appendRow(death)

        co = StandardItem('Colorado', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(co)
        case = StandardItem("cases: 13,441")
        death = StandardItem("deaths: 680")
        co.appendRow(case)
        co.appendRow(death)

        tn = StandardItem('Tennessee', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(tn)
        case = StandardItem("cases: 9,930")
        death = StandardItem("deaths: 183")
        tn.appendRow(case)
        tn.appendRow(death)

        nc = StandardItem('North Carolina', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nc)
        case = StandardItem("cases: 9,298")
        death = StandardItem("deaths: 328")
        nc.appendRow(case)
        nc.appendRow(death)

        ri = StandardItem('Rhode Island', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ri)
        case = StandardItem("cases: 7,708")
        death = StandardItem("deaths: 233")
        ri.appendRow(case)
        ri.appendRow(death)

        mo = StandardItem('Missouri', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(mo)
        case = StandardItem("cases: 7,253")
        death = StandardItem("deaths: 299")
        mo.appendRow(case)
        mo.appendRow(death)

        az = StandardItem('Arizona', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(az)
        case = StandardItem("cases: 6,725")
        death = StandardItem("deaths: 275")
        az.appendRow(case)
        az.appendRow(death)

        al = StandardItem('Alabama', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(al)
        case = StandardItem("cases: 6,467")
        death = StandardItem("deaths: 219")
        al.appendRow(case)
        al.appendRow(death)

        ms = StandardItem('Mississippi', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ms)
        case = StandardItem("cases: 6,094")
        death = StandardItem("deaths: 229")
        ms.appendRow(case)
        ms.appendRow(death)

        wi = StandardItem('Wisconsin', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(wi)
        case = StandardItem("cases: 6,081")
        death = StandardItem("deaths: 280")
        wi.appendRow(case)
        wi.appendRow(death)

        ia = StandardItem('Iowa', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ia)
        case = StandardItem("cases: 5,868")
        death = StandardItem("deaths: 127")
        ia.appendRow(case)
        ia.appendRow(death)

        sc = StandardItem('South Carolina', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(sc)
        case = StandardItem("cases: 5,498")
        death = StandardItem("deaths: 174")
        sc.appendRow(case)
        sc.appendRow(death)

        nv = StandardItem('Nevada', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nv)
        case = StandardItem("cases: 4,693")
        death = StandardItem("deaths: 206")
        nv.appendRow(case)
        nv.appendRow(death)

        ut = StandardItem('Utah', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ut)
        case = StandardItem("cases: 4,236")
        death = StandardItem("deaths: 41")
        ut.appendRow(case)
        ut.appendRow(death)

        de = StandardItem('Delaware', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(de)
        case = StandardItem("cases: 4,162")
        death = StandardItem("deaths: 125")
        de.appendRow(case)
        de.appendRow(death)

        ky = StandardItem('Kentucky', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ky)
        case = StandardItem("cases: 4,078")
        death = StandardItem("deaths: 208")
        ky.appendRow(case)
        ky.appendRow(death)

        dc = StandardItem('District of Columbia', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(dc)
        case = StandardItem("cases: 3,892")
        death = StandardItem("deaths: 185")
        dc.appendRow(case)
        dc.appendRow(death)

        mn = StandardItem('Minnesota', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(mn)
        case = StandardItem("cases: 3,816")
        death = StandardItem("deaths: 286")
        mn.appendRow(case)
        mn.appendRow(death)

        ks = StandardItem('Kansas', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ks)
        case = StandardItem("cases: 3,302")
        death = StandardItem("deaths: 124")
        ks.appendRow(case)
        ks.appendRow(death)

        ok = StandardItem('Oklahoma', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ok)
        case = StandardItem("cases: 3,281")
        death = StandardItem("deaths: 197")
        ok.appendRow(case)
        ok.appendRow(death)

        ne = StandardItem('Nebraska', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ne)
        case = StandardItem("cases: 3,028")
        death = StandardItem("deaths: 56")
        ne.appendRow(case)
        ne.appendRow(death)

        ar = StandardItem('Arkansas', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ar)
        case = StandardItem("cases: 3,017")
        death = StandardItem("deaths: 50")
        ar.appendRow(case)
        ar.appendRow(death)

        nm = StandardItem('New Mexico', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nm)
        case = StandardItem("cases: 2,726")
        death = StandardItem("deaths: 99")
        nm.appendRow(case)
        nm.appendRow(death)
        
        ore = StandardItem('Oregon', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ore)
        case = StandardItem("cases: 2,354")
        death = StandardItem("deaths: 93")
        ore.appendRow(case)
        ore.appendRow(death)

        sd = StandardItem('Oregon', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(sd)
        case = StandardItem("cases: 2,212")
        death = StandardItem("deaths: 11")
        sd.appendRow(case)
        sd.appendRow(death)

        ida = StandardItem('Idaho', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ida)
        case = StandardItem("cases: 1,897")
        death = StandardItem("deaths: 56")
        ida.appendRow(case)
        ida.appendRow(death)

        nh = StandardItem('New Hampshire', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nh)
        case = StandardItem("cases: 1,894")
        death = StandardItem("deaths: 60")
        nh.appendRow(case)
        nh.appendRow(death)

        pr = StandardItem('Puerto Rico', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(pr)
        case = StandardItem("cases: 1,389")
        death = StandardItem("deaths: 84")
        pr.appendRow(case)
        pr.appendRow(death)

        wv = StandardItem('West Virginia', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(wv)
        case = StandardItem("cases: 1,055")
        death = StandardItem("deaths: 34")
        wv.appendRow(case)
        wv.appendRow(death)

        me= StandardItem('Maine', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(me)
        case = StandardItem("cases: 1,015")
        death = StandardItem("deaths: 50")
        me.appendRow(case)
        me.appendRow(death)

        nd = StandardItem('North Dakota', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nd)
        case = StandardItem("cases: 942")
        death = StandardItem("deaths: 19")
        nd.appendRow(case)
        nd.appendRow(death)
        
        vt = StandardItem('Vermont', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(vt)
        case = StandardItem("cases: 855")
        death = StandardItem("deaths: 47")
        vt.appendRow(case)
        vt.appendRow(death)

        hi = StandardItem('Hawaii', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(hi)
        case = StandardItem("cases: 606")
        death = StandardItem("deaths: 14")
        hi.appendRow(case)
        hi.appendRow(death)

        wy = StandardItem('Wyoming', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(wy)
        case = StandardItem("cases: 502")
        death = StandardItem("deaths: 7")
        wy.appendRow(case)
        wy.appendRow(death)

        mt = StandardItem('Montana', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(mt)
        case = StandardItem("cases: 449")
        death = StandardItem("deaths: 14")
        mt.appendRow(case)
        mt.appendRow(death)

        ak = StandardItem('Alaska', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ak)
        case = StandardItem("cases: 344")
        death = StandardItem("deaths: 9")
        ak.appendRow(case)
        ak.appendRow(death)

        gm = StandardItem('Guam', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(gm)
        case = StandardItem("cases: 141")
        death = StandardItem("deaths: 5")
        gm.appendRow(case)
        gm.appendRow(death)

        vi = StandardItem('Virgin Islands', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(vi)
        case = StandardItem("cases: 57")
        death = StandardItem("deaths: 4")
        vi.appendRow(case)
        vi.appendRow(death)
        
        rootNodeUS.appendRow(usa)
        treeViewUS.setModel(treeModelUS)

        #Mexico Tree View
        treeViewMx = QTreeView(self)
        treeViewMx.setHeaderHidden(True)
        treeViewMx.setFixedWidth(380)
        treeViewMx.setFixedHeight(800)
       
        treeViewMx.setStyleSheet('QTreeView {\
                          margin: left;\
                          background-color:lightgray;\
                          border-style: inset;\
                          border-width: 2px;\
                          border-corlor: beige;\
                          padding: 2px;\
                          }')

        treeModelMx = QStandardItemModel()
        rootNodeMx = treeModelMx.invisibleRootItem()

        # Mexico Data
        
        mexico = StandardItem('Mexico', 14, set_bold=True, color=QColor(0, 153, 0))

        mc = StandardItem(mexicoCovData[0][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(mc)
        case = StandardItem("cases: " + str(mexicoCovData[0][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[0][2]))
        mc.appendRow(case)
        mc.appendRow(death)

        sm = StandardItem(mexicoCovData[1][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(sm)
        case = StandardItem("cases: " + str(mexicoCovData[1][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[1][2]))
        sm.appendRow(case)
        sm.appendRow(death)

        bc = StandardItem(mexicoCovData[2][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(bc)
        case = StandardItem("cases: " + str(mexicoCovData[2][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[2][2]))
        bc.appendRow(case)
        bc.appendRow(death)

        to = StandardItem(mexicoCovData[3][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(to)
        case = StandardItem("cases: " + str(mexicoCovData[3][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[3][2]))
        to.appendRow(case)
        to.appendRow(death)

        sa = StandardItem(mexicoCovData[4][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(sa)
        case = StandardItem("cases: " + str(mexicoCovData[4][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[4][2]))
        sa.appendRow(case)
        sa.appendRow(death)

        qr = StandardItem(mexicoCovData[5][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(qr)
        case = StandardItem("cases: " + str(mexicoCovData[5][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[5][2]))
        qr.appendRow(case)
        qr.appendRow(death)

        pu = StandardItem(mexicoCovData[6][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(pu)
        case = StandardItem("cases: " + str(mexicoCovData[6][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[6][2]))
        pu.appendRow(case)
        pu.appendRow(death)
        
        vz = StandardItem(mexicoCovData[7][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(vz)
        case = StandardItem("cases: " + str(mexicoCovData[7][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[7][2]))
        vz.appendRow(case)
        vz.appendRow(death)

        coa = StandardItem(mexicoCovData[8][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(coa)
        case = StandardItem("cases: " + str(mexicoCovData[8][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[8][2]))
        coa.appendRow(case)
        coa.appendRow(death)

        yu = StandardItem(mexicoCovData[9][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(yu)
        case = StandardItem("cases: " + str(mexicoCovData[9][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[9][2]))
        yu.appendRow(case)
        yu.appendRow(death)

        jo = StandardItem(mexicoCovData[10][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(jo)
        case = StandardItem("cases: " + str(mexicoCovData[10][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[10][2]))
        jo.appendRow(case)
        jo.appendRow(death)

        ts = StandardItem(mexicoCovData[11][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(ts)
        case = StandardItem("cases: " + str(mexicoCovData[11][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[11][2]))
        ts.appendRow(case)
        ts.appendRow(death)

        bjs = StandardItem(mexicoCovData[12][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(bjs)
        case = StandardItem("cases: " + str(mexicoCovData[12][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[12][2]))
        bjs.appendRow(case)
        bjs.appendRow(death)

        nl = StandardItem(mexicoCovData[13][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(nl)
        case = StandardItem("cases: " + str(mexicoCovData[13][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[13][2]))
        nl.appendRow(case)
        nl.appendRow(death)

        chi = StandardItem(mexicoCovData[14][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(chi)
        case = StandardItem("cases: " + str(mexicoCovData[14][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[14][2]))
        chi.appendRow(case)
        chi.appendRow(death)

        gu = StandardItem(mexicoCovData[15][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(gu)
        case = StandardItem("cases: " + str(mexicoCovData[15][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[15][2]))
        gu.appendRow(case)
        gu.appendRow(death)

        gue = StandardItem(mexicoCovData[16][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(gue)
        case = StandardItem("cases: " + str(mexicoCovData[16][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[16][2]))
        gue.appendRow(case)
        gue.appendRow(death)

        mic = StandardItem(mexicoCovData[17][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(mic)
        case = StandardItem("cases: " + str(mexicoCovData[17][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[17][2]))
        mic.appendRow(case)
        mic.appendRow(death)
        
        mor = StandardItem(mexicoCovData[18][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(mor)
        case = StandardItem("cases: " + str(mexicoCovData[18][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[18][2]))
        mor.appendRow(case)
        mor.appendRow(death)

        hid = StandardItem(mexicoCovData[19][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(hid)
        case = StandardItem("cases: " + str(mexicoCovData[19][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[19][2]))
        hid.appendRow(case)
        hid.appendRow(death)

        so = StandardItem(mexicoCovData[20][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(so)
        case = StandardItem("cases: " + str(mexicoCovData[20][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[20][2]))
        so.appendRow(case)
        so.appendRow(death)

        ag = StandardItem(mexicoCovData[21][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(ag)
        case = StandardItem("cases: " + str(mexicoCovData[21][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[21][2]))
        ag.appendRow(case)
        ag.appendRow(death)
        
        tl = StandardItem(mexicoCovData[22][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(tl)
        case = StandardItem("cases: " + str(mexicoCovData[22][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[22][2]))
        tl.appendRow(case)
        tl.appendRow(death)

        cs = StandardItem(mexicoCovData[23][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(cs)
        case = StandardItem("cases: " + str(mexicoCovData[23][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[23][2]))
        cs.appendRow(case)
        cs.appendRow(death)

        qo = StandardItem(mexicoCovData[24][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(qo)
        case = StandardItem("cases: " + str(mexicoCovData[24][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[24][2]))
        qo.appendRow(case)
        qo.appendRow(death)

        oa = StandardItem(mexicoCovData[25][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(oa)
        case = StandardItem("cases: " + str(mexicoCovData[25][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[25][2]))
        oa.appendRow(case)
        oa.appendRow(death)

        slp = StandardItem(mexicoCovData[26][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(slp)
        case = StandardItem("cases: " + str(mexicoCovData[26][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[26][2]))
        slp.appendRow(case)
        slp.appendRow(death)

        ce = StandardItem(mexicoCovData[27][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(ce)
        case = StandardItem("cases: " + str(mexicoCovData[27][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[27][2]))
        ce.appendRow(case)
        ce.appendRow(death)

        zs = StandardItem(mexicoCovData[28][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(zs)
        case = StandardItem("cases: " + str(mexicoCovData[28][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[28][2]))
        zs.appendRow(case)
        zs.appendRow(death)

        nt = StandardItem(mexicoCovData[29][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(nt)
        case = StandardItem("cases: " + str(mexicoCovData[29][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[29][2]))
        nt.appendRow(case)
        nt.appendRow(death)

        do = StandardItem(mexicoCovData[30][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(do)
        case = StandardItem("cases: " + str(mexicoCovData[30][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[30][2]))
        do.appendRow(case)
        do.appendRow(death)

        col = StandardItem(mexicoCovData[31][0], set_bold=True, color=QColor(102, 102, 0))
        mexico.appendRow(col)
        case = StandardItem("cases: " + str(mexicoCovData[31][1]))
        death = StandardItem("deaths: " + str(mexicoCovData[31][2]))
        col.appendRow(case)
        col.appendRow(death)

        rootNodeMx.appendRow(mexico)
        treeViewMx.setModel(treeModelMx)
        
        topright = QLabel('North Ameica Map')
        topright.setFixedWidth(1000)
        topright.setFixedHeight(800)
        topright.setAlignment(Qt.AlignRight
                              )
        bottom1 = QPushButton('Refresh Butotn')
        bottom1.setStyleSheet('QPushButton {\
                          margin: left;\
                          font: bold 14px;\
                          background-color:lightblue;\
                          color:white;\
                          border-style: inset;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-corlor: beige;\
                          padding: 6px;\
                          }')

        bottom1.setFixedWidth(180)
        bottom1.setFixedHeight(80)

        bottom2 = QPushButton('Source Button')
        bottom2.setStyleSheet('QPushButton {\
                          margin: left;\
                          font: bold 14px;\
                          background-color:lightgray;\
                          color:white;\
                          border-style: inset;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-corlor: beige;\
                          padding: 6px;\
                          }')

        bottom2.setFixedWidth(180)
        bottom2.setFixedHeight(80)
        
        bottom3 = QPushButton('Devs Button')
        bottom3.setStyleSheet('QPushButton {\
                          margin: left;\
                          font: bold 14px;\
                          background-color: purple;\
                          color:white;\
                          border-style: inset;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-corlor: beige;\
                          padding: 6px;\
                          }')

        bottom3.setFixedWidth(180)
        bottom3.setFixedHeight(80)                            

        h_splitter = QSplitter(Qt.Horizontal)
        h_splitter.addWidget(treeView)
        h_splitter.addWidget(treeViewUS)
        h_splitter.addWidget(treeViewMx)
        h_splitter.addWidget(topright)

        vtop_splitter = QSplitter(Qt.Vertical)
        vtop_splitter.addWidget(h_splitter)
        vtop_splitter.addWidget(bottom1)
        vtop_splitter.addWidget(bottom2)
        vtop_splitter.addWidget(bottom3)
        
        hbox.addWidget(vtop_splitter)

        self.setLayout(hbox)
        self.show()

def getMexicoData():
    with open('mexicoData.csv') as countryData:
        csv_reader = csv.reader(countryData, delimiter=',')
        for row in csv_reader:
            mexicoCovData.append([row[0], row[1], row[2]])
    
if __name__ == '__main__':
    mexicoSoup.scrapeMexico()
    mexicoSoup.mexicoToCSV()
    getMexicoData()
    app = QApplication(sys.argv)
    cs = MainWindow()
    sys.exit(app.exec_())


    
