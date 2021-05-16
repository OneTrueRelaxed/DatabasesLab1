INSERT INTO DisciplineTable(OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball,
                  AdaptScale)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.UkrPTName) as schoolid,
       (SELECT DISTINCT UkrTest FROM FirstTable WHERE UkrTest != 'null') as discipline,
       UkrTestStatus,
       UkrBall100,
       UkrBall12,
       UkrBall,
       UkrAdaptScale
FROM FirstTable WHERE FirstTable.UkrTest != 'null';
/*   AND FirstTable.UkrTestStatus != 'null'
   AND FirstTable.UkrPTName != 'null'
   AND FirstTable.UkrPTRegName != 'null'
   AND FirstTable.UkrPTAreaName != 'null'
   AND FirstTable.UkrPTTerName != 'null'
   AND FirstTable.UkrBall100 IS NOT NULL
   AND FirstTable.UkrBall12 IS NOT NULL
   AND FirstTable.UkrBall IS NOT NULL;*/

INSERT INTO DisciplineTable (OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.histPTName) as schoolid,
       (SELECT DISTINCT histTest FROM FirstTable WHERE histTest != 'null') as discipline,
       histTestStatus,
       histBall100,
       histBall12,
       histBall

FROM FirstTable WHERE FirstTable.histTest != 'null';

INSERT INTO DisciplineTable (OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.mathPTName) as schoolid,
       (SELECT DISTINCT mathTest FROM FirstTable WHERE mathTest != 'null') as discipline,
       mathTestStatus,
       mathBall100,
       mathBall12,
       mathBall

FROM FirstTable WHERE FirstTable.mathTest != 'null';

INSERT INTO DisciplineTable (OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.physPTName) as schoolid,
       (SELECT DISTINCT physTest FROM FirstTable WHERE physTest != 'null') as discipline,
       physTestStatus,
       physBall100,
       physBall12,
       physBall

FROM FirstTable WHERE FirstTable.physTest != 'null';

INSERT INTO DisciplineTable (OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.chemPTName) as schoolid,
       (SELECT DISTINCT chemTest FROM FirstTable WHERE chemTest != 'null') as discipline,
       chemTestStatus,
       chemBall100,
       chemBall12,
       chemBall

FROM FirstTable WHERE FirstTable.chemTest != 'null';
INSERT INTO DisciplineTable (OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.bioPTName) as schoolid,
       (SELECT DISTINCT bioTest FROM FirstTable WHERE bioTest != 'null') as discipline,
       bioTestStatus,
       bioBall100,
       bioBall12,
       bioBall

FROM FirstTable WHERE FirstTable.bioTest != 'null';
INSERT INTO DisciplineTable (OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.geoPTName) as schoolid,
       (SELECT DISTINCT geoTest FROM FirstTable WHERE geoTest != 'null') as discipline,
       geoTestStatus,
       geoBall100,
       geoBall12,
       geoBall

FROM FirstTable WHERE FirstTable.geoTest != 'null';
INSERT INTO DisciplineTable (OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball,
                  DPALevel)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.engPTName) as schoolid,
       (SELECT DISTINCT engTest FROM FirstTable WHERE engTest != 'null') as discipline,
       engTestStatus,
       engBall100,
       engBall12,
       engBall,
       engDPALevel

FROM FirstTable WHERE FirstTable.engTest != 'null';
INSERT INTO DisciplineTable (OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball,
                  DPALevel)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.fraPTName) as schoolid,
       (SELECT DISTINCT fraTest FROM FirstTable WHERE fraTest != 'null') as discipline,
       fraTestStatus,
       fraBall100,
       fraBall12,
       fraBall,
       fraDPALevel

FROM FirstTable WHERE FirstTable.fraTest != 'null';
INSERT INTO DisciplineTable (OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball,
                  DPALevel)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.deuPTName) as schoolid,
       (SELECT DISTINCT deuTest FROM FirstTable WHERE deuTest != 'null') as discipline,
       deuTestStatus,
       deuBall100,
       deuBall12,
       deuBall,
       deuDPALevel

FROM FirstTable WHERE FirstTable.deuTest != 'null';
INSERT INTO DisciplineTable (OUTID,
                  SchoolID,
                  Test,
                  TestStatus,
                  Ball100,
                  Ball12,
                  Ball,
                  DPALevel)
SELECT FirstTable.OUTID,
       (SELECT SchoolID from School WHERE Name = FirstTable.spaPTName) as schoolid,
       (SELECT DISTINCT spaTest FROM FirstTable WHERE spaTest != 'null') as discipline,
       spaTestStatus,
       spaBall100,
       spaBall12,
       spaBall,
       spaDPALevel

FROM FirstTable WHERE FirstTable.spaTest != 'null';