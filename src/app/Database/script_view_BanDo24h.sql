USE [BDSG]
GO

/****** Object:  View [dbo].[vw_CongTy_Fax]    Script Date: 07/06/2012 11:38:25 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE VIEW [dbo].[vw_CongTy_Fax]
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

CREATE VIEW [dbo].[vw_CongTy_DienThoai]
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

CREATE VIEW [dbo].[vw_CongTy_NganhNghe]
AS
SELECT	i.CongTyId, STUFF(g.y, 1, 1, '') AS NganhNghe
FROM	
(SELECT	m.CongTyId FROM	(select CongTyId,Ten
FROM tbl_CongTy_NganhNghe ctnn
LEFT JOIN tbl_NganhNghe nn
ON ctnn.NganhNgheId = nn.Id) as m GROUP BY CongTyId ) AS i 
CROSS APPLY	( 
	SELECT DISTINCT	',' + CAST(Ten AS NVARCHAR(4000)) 
	FROM	 (select CongTyId,Ten
			FROM tbl_CongTy_NganhNghe ctnn
			LEFT JOIN tbl_NganhNghe nn
			ON ctnn.NganhNgheId = nn.Id) AS s 
	WHERE	 s.CongTyId = i.CongTyId 
	ORDER BY	',' + CAST(Ten AS NVARCHAR(4000)) 
	FOR XML	 PATH('') 
	) 
AS g(y)


GO

CREATE VIEW [dbo].[vw_CongTy]
AS
SELECT ct.Id,Ten,DiaChiChinhXac,SoDienThoai,Email,SoFax,Website,Rank,SoNha,Duong,Phuong,Quan,DuongKhongDau,QuanKhongDau,NganhNghe,X,Y
FROM tbl_CongTy ct
LEFT JOIN tbl_DiaChi dc
ON ct.DiaChiId = dc.Id
LEFT JOIN vw_CongTy_DienThoai dt 
ON ct.Id = dt.CongTyId 
LEFT JOIN vw_CongTy_Fax sf 
ON ct.Id = sf.CongTyId
LEFT JOIN vw_CongTy_NganhNghe nn
ON ct.Id = nn.CongTyId


GO


