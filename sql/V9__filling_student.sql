INSERT INTO StudentTable (OUTID,
                     AreaID,
                     SchoolID,
                     Birth,
                     SexTypeName,
                     RegTypeName,
                     ClassProfileName,
                     ClassLangName
)
SELECT OUTID,
        (SELECT AreaID
        FROM Area
        WHERE FirstTable.RegTypeName = Area.RegName
          AND FirstTable.AreaName = Area.AreaName
          AND FirstTable.TerName = Area.TerName) as areaid,
       (SELECT SchoolID
        FROM School
        WHERE FirstTable.EOName = School.Name)   as schoolid,
       Birth,
       SexTypeName,
       RegTypeName,
       ClassProfileName,
       ClassLangName

FROM FirstTable;
