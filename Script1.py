import arcpy

aWS = r"C:\Khalid\Assignment_03\Assignment_03\Assignment_03.gdb"
arcpy.env.workspace = aWS

aFC = "LandParcels"

with arcpy.da.UpdateCursor(aFC, "*",'TaxVal04 > 100 AND TaxVal06 > 100') as aCursor:
    for aRow in aCursor:
        aRow[6]= ((aRow[2]-aRow[3])/aRow[3])
        if aRow[6]<-0.03:
            aRow[7]="A"
        if aRow[6]<0 and aRow[6]>=-0.03:
            aRow[7]="B"
        if aRow[6]== 0:
            aRow[7]="C"
        if aRow[6]>0 and aRow[6]<=3:
            aRow[7]="D"
        if aRow[6]>3:
            aRow[7]="E"
        


        
            
        aCursor.updateRow(aRow)
        

del aRow
del aCursor
import datetime
Atime=datetime.datetime.now()
aFile= open(r"C:\Khalid\Assignment_03\msg.txt", "w")
aFile.write(str(Atime))
aFile.close()

