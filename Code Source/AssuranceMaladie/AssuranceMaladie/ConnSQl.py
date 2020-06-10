import pyodbc
import random
from .models import Assurance

def Connexion():
    server = 'MASTER-ACER\FAKIRISQL'
    db1 = 'Assurance Maladie'
    tcon = 'yes'
    return pyodbc.connect(driver='{SQL Server}', host=server, database=db1,trusted_connection=tcon)

def allVille():
    cur=Connexion().cursor().execute("SELECT Cpam FROM [dbo].[dim_Cpam Affiliation Bénéficiaire] ORDER BY Cpam")
    rows = cur.fetchall()
    villes=list()
    i=0
    for row in rows:
	    villes.append(row[0])
	    i=i+1
    return villes

def allNatureAssu():
    cur=Connexion().cursor().execute("SELECT asuNat FROM [dbo].[dim_Nature Assurance] ORDER BY asuNat")
    rows = cur.fetchall()
    natAssus=list()
    i=0
    for row in rows:
	    natAssus.append(row[0])
	    i=i+1
    return natAssus

def allSpecialite():
    cur=Connexion().cursor().execute("SELECT preSpe FROM [dbo].[dim_Spécialité Prescripteur] ORDER BY preSpe")
    rows = cur.fetchall()
    specil=list()
    i=0
    for row in rows:
	    specil.append(row[0])
	    i=i+1
    return specil

def allQualite():
    cur=Connexion().cursor().execute("SELECT benQlt FROM [dbo].[dim_Qualité Bénéficiaire] ORDER BY benQlt")
    rows = cur.fetchall()
    Qual=list()
    i=0
    for row in rows:
	    Qual.append(row[0])
	    i=i+1
    return Qual

def allManExe():
    cur=Connexion().cursor().execute("SELECT mode FROM [dbo].[dim_Mode Exercice] ORDER BY mode")
    rows = cur.fetchall()
    manExe=list()
    i=0
    for row in rows:
	    manExe.append(row[0])
	    i=i+1
    return manExe

def allPrestation():
    cur=Connexion().cursor().execute("SELECT prsNat FROM [dbo].[dim_Prestation] ORDER BY prsNat")
    rows = cur.fetchall()
    prsNat=list()
    i=0
    for row in rows:
	    prsNat.append(row[0])
	    i=i+1
    return prsNat

def allSelections():
    return (allVille(),allNatureAssu(),allSpecialite(),allQualite(),allPrestation(),allManExe())

def natuAssById(id):
    cur=Connexion().cursor()
    cur.execute("SELECT [asuNat] FROM [dbo].[dim_Nature Assurance] WHERE [ID_asuNat]='"+str(id)+"'")
    return cur.fetchone()[0]

def villeById(id):
    cur=Connexion().cursor()
    cur.execute("SELECT [Cpam] FROM [dbo].[dim_Cpam Affiliation Bénéficiaire] Where ID_Cpam='"+str(id)+"'")
    return cur.fetchone()[0]

def SpeById(id):
    cur=Connexion().cursor()
    cur.execute("SELECT [preSpe] FROM [dbo].[dim_Spécialité Prescripteur] WHERE [ID_preSpe]='"+str(id)+"'")
    return cur.fetchone()[0]

def modeById(id):
    cur=Connexion().cursor()
    cur.execute("SELECT [mode] FROM [dbo].[dim_Mode Exercice] WHERE [ID_mode]='"+str(id)+"'")
    return cur.fetchone()[0]

def presById(id):
    cur=Connexion().cursor()
    cur.execute("SELECT [prsNat] FROM [dbo].[dim_Prestation] WHERE [ID_prsNat]='"+str(id)+"'")
    return cur.fetchone()[0]

def qualById(id):
    cur=Connexion().cursor()
    cur.execute("SELECT [benQlt] FROM [dbo].[dim_Qualité Bénéficiaire] WHERE [ID_benQlt]='"+str(id)+"'")
    return cur.fetchone()[0]

def insertToDB(natAs,sp,mn,pr,ql,v,tr,br,d):
    cur=Connexion().cursor()
    cur.execute("SELECT DISTINCT f.idVille,f.idDep,f.idReg FROM [dbo].[VDR] as f CROSS JOIN [dbo].[dim_Cpam Affiliation Bénéficiaire] as v where v.ID_Cpam=f.idVille and v.Cpam ='"+v+"'")
    row = cur.fetchone()
    idville=row[0]; idDep=row[1]; idReg=row[2]
    cur.execute("SELECT [ID_prsNat] FROM [dbo].[dim_Prestation] WHERE [prsNat]='"+pr+"'")
    row = cur.fetchone()
    idPre=row[0]; ssDate=d
    cur.execute("SELECT [ID_asuNat] FROM [dbo].[dim_Nature Assurance] WHERE [asuNat]='"+natAs+"'")
    row = cur.fetchone()
    idNatAs=row[0]
    cur.execute("SELECT [ID_benQlt] FROM [dbo].[dim_Qualité Bénéficiaire] WHERE [benQlt]='"+ql+"'")
    row = cur.fetchone()
    idQl=row[0]; remTaux=int(tr)
    cur.execute("SELECT [ID_preSpe] FROM [dbo].[dim_Spécialité Prescripteur] WHERE [preSpe]='"+sp+"'")
    row = cur.fetchone()
    idSpe=row[0]
    cur.execute("SELECT [ID_mode] FROM [dbo].[dim_Mode Exercice] WHERE [mode]='"+mn+"'")
    row = cur.fetchone()
    idMode=row[0]; recMon=int(br); remMon=remTaux*recMon/100
    actDnb=coef=random.randrange(2,20); depMon=random.randrange(0,130)
    tt=(idville,idDep,idReg,idPre,ssDate,idNatAs,idQl,remTaux,idSpe,idMode,remMon,recMon,depMon,coef,actDnb)
    cur.execute("INSERT INTO [dbo].[fact_Assurance] ([cpam],[dpt],[region],[prs_nat],[sns_date],[asu_nat],[ben_qlt],[REM_TAU],[pre_spe],[pre_stj1],[rem_mon],[rec_mon],[dep_mon],[act_coe],[act_dnb]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",tt)
    cur.commit()

def listAssurance():
    cur=Connexion().cursor()
    cur.execute("SELECT TOP (500) [id],[cpam],[asu_nat],[ben_qlt],[rem_mon] FROM [dbo].[fact_Assurance]")
    rows=cur.fetchall()
    listes=dict()
    for row in rows:
            a=list()
            a=(villeById(row[1]),natuAssById(row[2]),qualById(row[3]),str(row[4]))
            listes[row[0]]=a
    return listes

def getAssuranceByID(id):
    cur=Connexion().cursor()
    cur.execute("SELECT * FROM [dbo].[fact_Assurance] WHERE [id]='"+str(id)+"'")
    row=cur.fetchone()
    assu=Assurance()
    assu.id=row[0]
    assu.ville=villeById(row[1])
    assu.natureAssurance=natuAssById(row[6])
    assu.specialiteExecute=SpeById(row[9])
    assu.manierExecuter=modeById(row[10])
    assu.prestation=presById(row[4])
    assu.qualiteBenificiaire=qualById(row[7])
    assu.tauxRemb=row[8]
    assu.baseRemb=row[12]
    assu.dateRemb=str(row[5])
    assu.monRem=assu.tauxRemb*assu.baseRemb/100
    return assu

def ModierAssur(id,v,nat,sp,mod,pre,ql,tr,br,dateR):
    cur=Connexion().cursor()
    cur.execute("SELECT DISTINCT f.idVille,f.idDep,f.idReg FROM [dbo].[VDR] as f CROSS JOIN [dbo].[dim_Cpam Affiliation Bénéficiaire] as v where v.ID_Cpam=f.idVille and v.Cpam ='"+v+"'")
    row = cur.fetchone()
    idville=row[0]; idDep=row[1]; idReg=row[2]
    cur.execute("SELECT [ID_prsNat] FROM [dbo].[dim_Prestation] WHERE [prsNat]='"+pre+"'")
    row = cur.fetchone()
    idPre=row[0]; ssDate=dateR
    cur.execute("SELECT [ID_asuNat] FROM [dbo].[dim_Nature Assurance] WHERE [asuNat]='"+nat+"'")
    row = cur.fetchone()
    idNatAs=row[0]
    cur.execute("SELECT [ID_benQlt] FROM [dbo].[dim_Qualité Bénéficiaire] WHERE [benQlt]='"+ql+"'")
    row = cur.fetchone()
    idQl=row[0]; remTaux=int(tr)
    cur.execute("SELECT [ID_preSpe] FROM [dbo].[dim_Spécialité Prescripteur] WHERE [preSpe]='"+sp+"'")
    row = cur.fetchone()
    idSpe=row[0]
    cur.execute("SELECT [ID_mode] FROM [dbo].[dim_Mode Exercice] WHERE [mode]='"+mod+"'")
    row = cur.fetchone()
    idMode=row[0]; recMon=int(br); remMon=remTaux*recMon/100
    actDnb=coef=random.randrange(2,20); depMon=random.randrange(0,130)
    tt=(idville,idDep,idReg,idPre,ssDate,idNatAs,idQl,remTaux,idSpe,idMode,remMon,recMon,depMon,coef,actDnb,id)
    cur.execute("UPDATE [dbo].[fact_Assurance] SET [cpam]=?,[dpt]=?,[region]=?,[prs_nat]=?,[sns_date]=?,[asu_nat]=?,[ben_qlt]=?,[REM_TAU]=?,[pre_spe]=?,[pre_stj1]=?,[rem_mon]=?,[rec_mon]=?,[dep_mon]=?,[act_coe]=?,[act_dnb]=? WHERE id=?",tt)
    cur.commit()

def SupprimerAssur(id):
    cur=Connexion().cursor()
    cur.execute("DELETE FROM [dbo].[fact_Assurance] WHERE id=?",id)
    cur.commit()


