INSERT INTO Area (RegName,
                  AreaName,
                  TerName,
                  TerTypeName)
SELECT DISTINCT Regname,
                AreaName,
                TerName,
                TerTypeName
FROM FirstTable
ON CONFLICT DO NOTHING;


INSERT INTO Area (RegName,
                  AreaName,
                  TerName)
SELECT DISTINCT EORegName,
                EOAreaName,
                EOTerName
FROM FirstTable
ON CONFLICT DO NOTHING;