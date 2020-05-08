import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QFont, QPixmap
from PyQt5.QtCore import *
from PyQt5.Qt import QStandardItemModel, QStandardItem
import mexicoSoup
import canadaSoup
import usaSoup

mexicoCovData = []
canadaCovData = []
usaCovData = []

class StandardItem(QStandardItem):
    def __init__(self, text='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        font = QFont('Courier New', font_size)
        font.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(font)
        self.setText(text)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('PROJECT CODE SCRAPPERS')
        self.setGeometry(30,30, 2000, 1200)

        hbox = QHBoxLayout()

        # Create Canada Tree View
        treeView = QTreeView(self)
        treeView.setHeaderHidden(True)
        treeView.setFixedWidth(380)
        treeView.setFixedHeight(850)
        treeView.move(10, 5)
        treeView.setStyleSheet('QTreeView {\
                          margin: left;\
                          background-color:#FFFAFA;\
                          border-style: solid;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-corlor: gray;\
                          padding: 6px;}')

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()
      
        # Canada Data
        canada = StandardItem('Canada', 14, set_bold=True, color=QColor(255, 0, 0))

        nl = StandardItem('Newfoundland and Labrador', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(nl)
        case = StandardItem("cases: " + str(canadaCovData[1][1]))
        death = StandardItem("deaths: " + str(canadaCovData[1][2]))
        nl.appendRow(case)
        nl.appendRow(death)

        pe = StandardItem('Prince Edward Island', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(pe)
        case = StandardItem("cases: " + str(canadaCovData[2][1]))
        death = StandardItem("deaths: " + str(canadaCovData[2][2]))
        pe.appendRow(case)
        pe.appendRow(death)

        ns = StandardItem('Nova Scotia',set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(ns)
        case = StandardItem("cases: " + str(canadaCovData[3][1]))
        death = StandardItem("deaths: " + str(canadaCovData[3][2]))
        ns.appendRow(case)
        ns.appendRow(death)

        nb = StandardItem('New Brunswick', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(nb)
        case = StandardItem("cases: " + str(canadaCovData[4][1]))
        death = StandardItem("deaths: " + str(canadaCovData[4][2]))
        nb.appendRow(case)
        nb.appendRow(death)

        quebec = StandardItem('Quebec', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(quebec)
        case = StandardItem("cases: " + str(canadaCovData[5][1]))
        death = StandardItem("deaths: " + str(canadaCovData[5][2]))
        quebec.appendRow(case)
        quebec.appendRow(death)

        ontario = StandardItem('Ontario', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(ontario)
        case = StandardItem("cases: " + str(canadaCovData[6][1]))
        death = StandardItem("deaths: " + str(canadaCovData[6][2]))
        ontario.appendRow(case)
        ontario.appendRow(death)

        manitoba = StandardItem('Manitoba', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(manitoba)
        case = StandardItem("cases: " + str(canadaCovData[7][1]))
        death = StandardItem("deaths: " + str(canadaCovData[7][2]))
        manitoba.appendRow(case)
        manitoba.appendRow(death)

        saskatchewan = StandardItem('Saskatchewan', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(saskatchewan)
        case = StandardItem("cases: " + str(canadaCovData[8][1]))
        death = StandardItem("deaths: " + str(canadaCovData[8][2]))
        saskatchewan.appendRow(case)
        saskatchewan.appendRow(death)

        alberta = StandardItem('Alberta', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(alberta)
        case = StandardItem("cases: " + str(canadaCovData[9][1]))
        death = StandardItem("deaths: " + str(canadaCovData[9][2]))
        alberta.appendRow(case)
        alberta.appendRow(death)

        bc = StandardItem('Bristis Columbia', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(bc)
        case = StandardItem("cases: " + str(canadaCovData[10][1]))
        death = StandardItem("deaths: " + str(canadaCovData[10][2]))
        bc.appendRow(case)
        bc.appendRow(death)

        yukon = StandardItem('Yukon', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(yukon)
        case = StandardItem("cases: " + str(canadaCovData[11][1]))
        death = StandardItem("deaths: " + str(canadaCovData[11][2]))
        yukon.appendRow(case)
        yukon.appendRow(death)

        nt = StandardItem('Northwest Teritories', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(nt)
        case = StandardItem("cases: " + str(canadaCovData[12][1]))
        death = StandardItem("deaths: " + str(canadaCovData[12][2]))
        nt.appendRow(case)
        nt.appendRow(death)

        nunavut = StandardItem('Nunavut', set_bold=True, color=QColor(178, 34, 34))
        canada.appendRow(nunavut)
        case = StandardItem("cases: " + str(canadaCovData[13][1]))
        death = StandardItem("deaths: " + str(canadaCovData[13][2]))
        nunavut.appendRow(case)
        nunavut.appendRow(death)

        # Add canada data to rootnode and set the tree model for tree view
        rootNode.appendRow(canada)
        treeView.setModel(treeModel)

        # Create USA Tree View
        treeViewUS = QTreeView(self)
        treeViewUS.setHeaderHidden(True)
        treeViewUS.setFixedWidth(380)
        treeViewUS.setFixedHeight(850)
        treeViewUS.move(380, 5)
        treeViewUS.setStyleSheet('QTreeView {\
                          margin: left;\
                          background-color:#F0F8FF;\
                          border-style: inset;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-corlor: gray;\
                          padding: 6px;\
                          }')

        treeModelUS = QStandardItemModel()
        rootNodeUS = treeModelUS.invisibleRootItem()

        # USA Data
        usa = StandardItem('USA', 14, set_bold=True, color=QColor(0, 0, 204))

        ny = StandardItem('New York', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(ny)
        case = StandardItem("cases: ")
        death = StandardItem("deaths: ")
        ny.appendRow(case)
        ny.appendRow(death)

        nj = StandardItem('New Jersey', set_bold=True, color=QColor(76, 0, 153))
        usa.appendRow(nj)
        case = StandardItem("cases: ")
        death = StandardItem("deaths: ")
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

        # Add usa data to rootnode and set the tree model for tree view
        rootNodeUS.appendRow(usa)
        treeViewUS.setModel(treeModelUS)

        # Create Mexico Tree View
        treeViewMx = QTreeView(self)
        treeViewMx.setHeaderHidden(True)
        treeViewMx.setFixedWidth(380)
        treeViewMx.setFixedHeight(850)
        treeViewMx.move(750, 5)
       
        treeViewMx.setStyleSheet('QTreeView {\
                          margin: left;\
                          background-color: #F5FFFA;\
                          border-style: inset;\
                          border-width: 2px;\
                          border-radius: 10px;\
                          border-corlor: gray;\
                          padding: 6px;\
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

        # Add mexico data to rootnode and set the tree model for tree view
        rootNodeMx.appendRow(mexico)
        treeViewMx.setModel(treeModelMx)

        # North America Map
        mapNA = QFrame(self)
        mapNA.setFixedWidth(830)
        mapNA.setFixedHeight(880)
        mapNA.move(1130, 20)
        mapNA.setStyleSheet('QFrame {\
                              background-color:#F5F5F5;\
                              border: 6px gray solid;\
                              }')

        # Refesh Button                      
        refresh_btn = QPushButton('Refresh', self)
        refresh_btn.setStyleSheet('QPushButton {\
                          font: bold 16px;\
                          background-color:purple;\
                          color:white;\
                          border-style: inset;\
                          border-width: 3px;\
                          border-radius: 10px;\
                          border-corlor: beige;\
                          padding: 6px;\
                          }')

        refresh_btn.setFixedWidth(220)
        refresh_btn.setFixedHeight(80)
        refresh_btn.move(50, 900)
        refresh_btn.clicked.connect(self.onRefreshClicked)

        # Source Button
        source_btn = QPushButton('Source', self)
        source_btn.setStyleSheet('QPushButton {\
                          font: bold 16px;\
                          background-color:#FFB266;\
                          color:white;\
                          border-style: inset;\
                          border-width: 3px;\
                          border-radius: 10px;\
                          border-corlor: beige;\
                          padding: 6px;\
                          }')

        source_btn.setFixedWidth(220)
        source_btn.setFixedHeight(80)
        source_btn.move(300, 900)
        source_btn.clicked.connect(self.onSourceClicked)
        
        # Devs Button
        devs_btn = QPushButton('Developers', self)
        devs_btn.setStyleSheet('QPushButton {\
                          font: bold 16px;\
                          background-color: lightblue;\
                          color:white;\
                          border-style: inset;\
                          border-width: 3px;\
                          border-radius: 10px;\
                          border-corlor: beige;\
                          padding: 6px;\
                          }')

        devs_btn.setFixedWidth(220)
        devs_btn.setFixedHeight(80)                            
        devs_btn.move(550, 900)
        devs_btn.clicked.connect(self.onDevsClicked)

        quitButton = QPushButton('Quit', self)
        quitButton.setStyleSheet('QPushButton {\
                          font: bold 16px;\
                          background-color: gray;\
                          color:white;\
                          border-style: inset;\
                          border-width: 3px;\
                          border-radius: 10px;\
                          border-corlor: beige;\
                          padding: 6px;\
                          }')
        quitButton.setFixedWidth(220)
        quitButton.setFixedHeight(80)                            
        quitButton.move(800, 900)
        quitButton.clicked.connect(self.onQuitClicked)
        
        news = QTextEdit(self)
        news.setFixedWidth(800)
        news.setFixedHeight(200)
        news.move(1150, 980)
        
        
        hbox.addWidget(refresh_btn)
        hbox.addWidget(source_btn)
        hbox.addWidget(devs_btn)
        hbox.addWidget(news)
                   
        self.setLayout(hbox)
        self.show()

    def onRefreshClicked(self):
        refMsg = QMessageBox(self)

    def onSourceClicked(self, source):

        source = ("https://realpython.com/beautiful-soup-web-scraper-python \n" + \
                  "https://realpython.com/openpyxl-excel-spreadsheets-python \n" + \
                  "https://doc.qt.io/qt-5/stylesheet-reference.html \n" + \
                  "https://doc.qt.io/qtforpython/PySide2/QtGui/QFont.html#more \n" + \
                  "https://doc.qt.io/qtforpython/PySide2/QtWidgets/QTreeView.html \n" + \
                  "https://docs.python.org/3/howto/urllib2.html")
              
        sourceMsg = QMessageBox(self)
        sourceMsg.setWindowTitle('References: ')
        sourceMsg.move(400, 1100)
        sourceMsg.setText(source)
        sourceMsg.setStyleSheet('QMessageBox {\
                              font: 15px;\
                              font-family: georgia;\
                              background-color:#FFE5CC;\
                              padding: 6px;\
                              }')
        sourceMsg.exec_()

    def onDevsClicked(self):
        
        devsBox = QDiaglog(self)
        devsBox.setWindowTitle('Developed by: ')
        devsBox.setGeometry(100, 100, 500, 300)       
        labelImage = QLabel(self)
        pixmap = QPixmap("codeScrapers.png")
        labelImage.setPixmap(pixmap)
        devsBox.addWidget(labelImage)
#        self.setModel(True)
#        devsBox.exec_()
        devsBox.show()
        
    def onQuitClicked(self):
        sys.exit(app.exec_())
    
def getCanadaData():
        with open('canadaData.csv') as canData:
            csv_reader = csv.reader(canData, delimiter=',')
            for row in csv_reader:
                canadaCovData.append([row[0], row[1], row[2]])
            
def getUsaData():
        with open('usaData.csv') as usData:
            csv_reader = csv.reader(usData, delimiter=',')
            for row in csv_reader:
                usaCovData.append([row[0], row[1], row[2]])

def getMexicoData():
        with open('mexicoData.csv') as countryData:
            csv_reader = csv.reader(countryData, delimiter=',')
            for row in csv_reader:
                mexicoCovData.append([row[0], row[1], row[2]])   
   
if __name__ == '__main__':

    getMexicoData()
    getCanadaData()
    app = QApplication(sys.argv)
    codeScraper = MainWindow()
    sys.exit(app.exec_())


    
