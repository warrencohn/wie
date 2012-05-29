--DROP VIEW CongTy_NganhNghe_VW
GO
CREATE VIEW CongTy_DienThoai_VW
AS
SELECT	i.CongTyId, STUFF(g.y, 1, 1, '') AS SoDienThoai
	FROM	
	(SELECT	CongTyId FROM tbl_CongTy_DienThoai GROUP BY CongTyId ) AS i 
	CROSS APPLY	( 
	SELECT DISTINCT	',' + CAST(SoDienThoai AS VARCHAR(11)) 
	FROM	 tbl_CongTy_DienThoai AS s 
	WHERE	 s.CongTyId = i.CongTyId 
	ORDER BY	',' + CAST(SoDienThoai AS VARCHAR(11)) 
	FOR XML	 PATH('') 
	) AS g(y); 
	
GO
CREATE VIEW CongTy_Fax_VW
AS
SELECT	i.CongTyId, STUFF(g.y, 1, 1, '') AS SoFax
	FROM	
	(SELECT	CongTyId FROM tbl_CongTy_Fax GROUP BY CongTyId ) AS i 
	CROSS APPLY	( 
	SELECT DISTINCT	',' + CAST(SoFax AS VARCHAR(11)) 
	FROM	 tbl_CongTy_Fax AS s 
	WHERE	 s.CongTyId = i.CongTyId 
	ORDER BY	',' + CAST(SoFax AS VARCHAR(11)) 
	FOR XML	 PATH('') 
	) AS g(y)
GO	
CREATE VIEW CongTy_NganhNghe_VW
AS
SELECT	i.CongTyId, STUFF(g.y, 1, 1, '') AS NganhNghe
FROM	
(SELECT	m.CongTyId FROM	(select CongTyId,Ten
FROM tbl_CongTy_NganhNghe ctnn
LEFT JOIN tbl_NganhNghe nn
ON ctnn.NganhNgheId = nn.Id) as m GROUP BY CongTyId ) AS i 
CROSS APPLY	( 
	SELECT DISTINCT	',' + CAST(Ten AS VARCHAR(11)) 
	FROM	 (select CongTyId,Ten
			FROM tbl_CongTy_NganhNghe ctnn
			LEFT JOIN tbl_NganhNghe nn
			ON ctnn.NganhNgheId = nn.Id) AS s 
	WHERE	 s.CongTyId = i.CongTyId 
	ORDER BY	',' + CAST(Ten AS VARCHAR(11)) 
	FOR XML	 PATH('') 
	) 
AS g(y) 

GO
CREATE VIEW SEARCH_DIACHI_VW
AS
SELECT Ten,DiaChiChinhXac,SoDienThoai,Email,SoFax,Website,Rank,SoNha,Duong,Phuong,Quan,DuongKhongDau,QuanKhongDau,NganhNghe,X,Y
FROM tbl_CongTy ct
RIGHT JOIN tbl_DiaChi dc
ON ct.DiaChiId = dc.Id
LEFT JOIN CongTy_DienThoai_VW dt 
ON ct.Id = dt.CongTyId 
LEFT JOIN CongTy_Fax_VW sf 
ON ct.Id = sf.CongTyId
LEFT JOIN CongTy_NganhNghe_VW nn
ON ct.Id = nn.CongTyId
GO

SELECT * FROM SEARCH_DIACHI_VW
