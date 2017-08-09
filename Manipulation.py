'''
Created on Jun 1, 2017

@author: che
'''  
import csv


class Lead():
        class Datacenter():
            data = "Data Center Lifecycle Status" 
        class Enterprise():      
            enter = "Enterprise Lifecycle Status"
        class Ia():
            ia = "IA Lifecycle Status"
            
def __init__(lead):
    lead.inputFile = csv.reader(open("KNN_IN_Python.csv", "r"))
    lead.knnList = []
    lead.datacenter = ''
    lead.enterprise = ''
    lead.ia = ''
    lead.oem = ''
    lead.ic = ''
    lead.rev = ''
    lead.sic = ''


def loadCSV(lead):
    for row in lead.inputFile:
        leadObject = Lead()
        leadObject.setDatacenter(row[0])
        leadObject.setEnterprise(row[1])
        leadObject.setIa(row[2])
        leadObject.setOem(row[3])
        leadObject.setIc(row[4])
        leadObject.setRev(row[5])
        leadObject.setSic(row[6])

def getLeadDatacenter(lead):
    return lead.Datacenter

def getLeadEnterprise(lead):
    return lead.Enterprise

def getLeadIa(lead):
    return lead.Ia

def getLeadOem(lead):
    return lead.Oem

def getLeadIc(lead):
    return lead.Ic

def getLeadRev(lead):
    return lead.Rev

def getLeadSic(lead):
    return lead.Sic


with open('KNN_IN_Python.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
        print row

        
    
        