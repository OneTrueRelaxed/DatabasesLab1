INSERT INTO School (AreaID,
                    Name,
                    TypeName,
                    Parent)
SELECT DISTINCT (SELECT AreaID
                 FROM Area
                 WHERE FirstTable.EORegName = Area.RegName
                   AND FirstTable.EOAreaName = Area.AreaName
                   AND FirstTable.EOTerName = Area.TerName) as id,
                FirstTable.EOName,
                FirstTable.EOTypeName,
                FirstTable.EOParent
FROM FirstTable ON CONFLICT DO NOTHING;

INSERT INTO School (AreaID,
                    Name)
SELECT DISTINCT (SELECT AreaID
                 FROM Area
                 WHERE FirstTable.UkrPTRegName = Area.RegName
                   AND FirstTable.UkrPTAreaName = Area.AreaName
                   AND FirstTable.UkrPTTerName = Area.TerName) as id,
                FirstTable.UkrPTName
FROM FirstTable ON CONFLICT DO NOTHING;

INSERT INTO School (AreaID,
                    Name)
SELECT DISTINCT (SELECT AreaID
                 FROM Area
                 WHERE FirstTable.histPTRegName = Area.RegName
                   AND FirstTable.histPTAreaName = Area.AreaName
                   AND FirstTable.histPTTerName = Area.TerName) as id,
                FirstTable.histPTName
FROM FirstTable ON CONFLICT DO NOTHING;

INSERT INTO School (AreaID,
                    Name)
SELECT DISTINCT (SELECT AreaID
                 FROM Area
                 WHERE FirstTable.mathPTRegName = Area.RegName
                   AND FirstTable.mathPTAreaName = Area.AreaName
                   AND FirstTable.mathPTTerName = Area.TerName) as id,
                FirstTable.mathPTName
FROM FirstTable ON CONFLICT DO NOTHING;

INSERT INTO School (AreaID,
                    Name)
SELECT DISTINCT (SELECT AreaID
                 FROM Area
                 WHERE FirstTable.physPTRegName = Area.RegName
                   AND FirstTable.physPTAreaName = Area.AreaName
                   AND FirstTable.physPTTerName = Area.TerName) as id,
                FirstTable.physPTName
FROM FirstTable ON CONFLICT DO NOTHING;

INSERT INTO School (AreaID,
                    Name)
SELECT DISTINCT (SELECT AreaID
                 FROM Area
                 WHERE FirstTable.chemPTRegName = Area.RegName
                   AND FirstTable.chemPTAreaName = Area.AreaName
                   AND FirstTable.chemPTTerName = Area.TerName) as id,
                FirstTable.chemPTName
FROM FirstTable ON CONFLICT DO NOTHING;

INSERT INTO School (AreaID,
                    Name)
SELECT DISTINCT (SELECT AreaID
                 FROM Area
                 WHERE FirstTable.engPTRegName = Area.RegName
                   AND FirstTable.engPTAreaName = Area.AreaName
                   AND FirstTable.engPTTerName = Area.TerName) as id,
                FirstTable.engPTName
FROM FirstTable ON CONFLICT DO NOTHING;

INSERT INTO School (AreaID,
                    Name)
SELECT DISTINCT (SELECT AreaID
                 FROM Area
                 WHERE FirstTable.fraPTRegName = Area.RegName
                   AND FirstTable.fraPTAreaName = Area.AreaName
                   AND FirstTable.fraPTTerName = Area.TerName) as id,
                FirstTable.fraPTName
FROM FirstTable ON CONFLICT DO NOTHING;

INSERT INTO School (AreaID,
                    Name)
SELECT DISTINCT (SELECT AreaID
                 FROM Area
                 WHERE FirstTable.deuPTRegName = Area.RegName
                   AND FirstTable.deuPTAreaName = Area.AreaName
                   AND FirstTable.deuPTTerName = Area.TerName) as id,
                FirstTable.deuPTName
FROM FirstTable ON CONFLICT DO NOTHING;

INSERT INTO School (AreaID,
                    Name)
SELECT DISTINCT (SELECT AreaID
                 FROM Area
                 WHERE FirstTable.spaPTRegName = Area.RegName
                   AND FirstTable.spaPTAreaName = Area.AreaName
                   AND FirstTable.spaPTTerName = Area.TerName) as id,
                FirstTable.spaPTName
FROM FirstTable ON CONFLICT DO NOTHING;