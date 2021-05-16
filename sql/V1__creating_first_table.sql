CREATE TABLE IF NOT EXISTS FirstTable(
    OUTID UUID,
    Birth int,
    SEXTYPENAME varchar(10),
    REGNAME varchar(100),
    AREANAME varchar(100),
    TERNAME varchar(100),
    REGTYPENAME varchar(500),
    TerTypeName varchar(500),
    ClassProfileNAME varchar(500),
    ClassLangName varchar(500),
    EONAME varchar(400),
    EOTYPENAME varchar(100),
    EORegName varchar(100),
    EOAreaName varchar(100),
    EOTerName varchar(400),
    EOParent varchar(500),
    UkrTest varchar(500),
    UkrTestStatus varchar(100),
    UkrBall100 float ,
    UkrBall12 int ,
    UkrBall int ,
    UkrAdaptScale int ,
    UkrPTName varchar(500),
    UkrPTRegname varchar(500),
    UkrPTAreaName varchar(500),
    UkrPTTerName varchar(500),
    histTest varchar(500),
    HistLang varchar(500),
    histTestStatus varchar(100),
    histBall100 float,
    histBall12 int,
    histBall int,
    histPTName varchar(500),
    histPTRegname varchar(500),
    histPTAreaName varchar(500),
    histPTTerName varchar(500),
    mathTest varchar(500),
    mathLang varchar(20),
    mathTestStatus varchar(100),
    mathBall100 float ,
    mathBall12 int ,
    mathBall int ,
    mathPTName varchar(500),
    mathPTRegname varchar(500),
    mathPTAreaName varchar(500),
    mathPTTerName varchar(500),
    physTest varchar(500),
    physLang varchar(20),
    physTestStatus varchar(100),
    physBall100 float ,
    physBall12 int ,
    physBall int ,
    physPTName varchar(500),
    physPTRegname varchar(500),
    physPTAreaName varchar(500),
    physPTTerName varchar(500),
    chemTest varchar(500),
    chemLang varchar(20),
    chemTestStatus varchar(100),
    chemBall100 float ,
    chemBall12 int ,
    chemBall int ,
    chemPTName varchar(500),
    chemPTRegname varchar(500),
    chemPTAreaName varchar(500),
    chemPTTerName varchar(500),
    bioTest varchar(500),
    bioLang varchar(20),
    bioTestStatus varchar(100),
    bioBall100 float ,
    bioBall12 int ,
    bioBall int ,
    bioPTName varchar(500),
    bioPTRegname varchar(500),
    bioPTAreaName varchar(500),
    bioPTTerName varchar(500),
    geoTest varchar(500),
    geoLang varchar(20),
    geoTestStatus varchar(100),
    geoBall100 float ,
    geoBall12 int ,
    geoBall int ,
    geoPTName varchar(500),
    geoPTRegname varchar(500),
    geoPTAreaName varchar(500),
    geoPTTerName varchar(500),
    engTest varchar(500),
    engTestStatus varchar(100),
    engBall100 float ,
    engBall12 int ,
    engDPALevel varchar(400),
    engBall int ,
    engPTName varchar(500),
    engPTRegname varchar(500),
    engPTAreaName varchar(500),
    engPTTerName varchar(500),
    fraTest varchar(500),
    fraTestStatus varchar(100),
    fraBall100 float ,
    fraBall12 int ,
    fraDPALevel varchar(400),
    fraBall int ,
    fraPTName varchar(500),
    fraPTRegname varchar(500),
    fraPTAreaName varchar(500),
    fraPTTerName varchar(500),
    deuTest varchar(500),
    deuTestStatus varchar(100),
    deuBall100 float ,
    deuBall12 int ,
    deuDPALevel varchar(400),
    deuBall int ,
    deuPTName varchar(500),
    deuPTRegname varchar(500),
    deuPTAreaName varchar(500),
    deuPTTerName varchar(500),
    spaTest varchar(500),
    spaTestStatus varchar(100),
    spaBall100 float,
    spaBall12 int ,
    spaDPALevel varchar(400),
    spaBall int ,
    spaPTName varchar(500),
    spaPTRegname varchar(500),
    spaPTAreaName varchar(500),
    spaPTTerName varchar(500),
    Year int,
    PRIMARY KEY(OUTID, Year));