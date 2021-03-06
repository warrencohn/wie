USE [BDSG]
GO
/****** Object:  Table [dbo].[tbl_NganhNghe]    Script Date: 05/30/2012 08:52:03 ******/
SET IDENTITY_INSERT [dbo].[tbl_NganhNghe] ON
INSERT [dbo].[tbl_NganhNghe] ([Id], [Ten]) VALUES (1, N'Buon Ban')
INSERT [dbo].[tbl_NganhNghe] ([Id], [Ten]) VALUES (2, N'Dich Vu')
SET IDENTITY_INSERT [dbo].[tbl_NganhNghe] OFF
/****** Object:  Table [dbo].[tbl_DiaChi]    Script Date: 05/30/2012 08:52:03 ******/
SET IDENTITY_INSERT [dbo].[tbl_DiaChi] ON
INSERT [dbo].[tbl_DiaChi] ([Id], [SoNha], [Duong], [Phuong], [Quan], [DuongKhongDau], [QuanKhongDau], [IDConDuong], [IDQuan], [IDNha], [BangNha], [X], [Y]) VALUES (1, N'123', N'Lý Thường Kiệt', N'10', N'10', N'Ly Thuong Kiet', N'10', N'LTK100001', N'10100001', 123100001, NULL, 10.805728, 106.642726)
INSERT [dbo].[tbl_DiaChi] ([Id], [SoNha], [Duong], [Phuong], [Quan], [DuongKhongDau], [QuanKhongDau], [IDConDuong], [IDQuan], [IDNha], [BangNha], [X], [Y]) VALUES (2, N'333', N'Lý Thường Kiệt', N'7', N'7', N'Ly Thuong Kiet', N'10', N'LTK100001', N'10100001', 123100001, NULL, 10.771762, 106.687597)
INSERT [dbo].[tbl_DiaChi] ([Id], [SoNha], [Duong], [Phuong], [Quan], [DuongKhongDau], [QuanKhongDau], [IDConDuong], [IDQuan], [IDNha], [BangNha], [X], [Y]) VALUES (3, N'444', N'Trường Chinh', N'4', N'4', N'Truong Chinh', N'5', NULL, NULL, NULL, NULL, 10.823099, 106.629644)
INSERT [dbo].[tbl_DiaChi] ([Id], [SoNha], [Duong], [Phuong], [Quan], [DuongKhongDau], [QuanKhongDau], [IDConDuong], [IDQuan], [IDNha], [BangNha], [X], [Y]) VALUES (4, N'555', N'Trường Chinh', N'5', N'5', N'Truong Chinh', N'5', NULL, NULL, NULL, NULL, 10.785059, 106.641981)
SET IDENTITY_INSERT [dbo].[tbl_DiaChi] OFF
/****** Object:  Table [dbo].[tbl_CongTy]    Script Date: 05/30/2012 08:52:03 ******/
SET IDENTITY_INSERT [dbo].[tbl_CongTy] ON
INSERT [dbo].[tbl_CongTy] ([Id], [Ten], [DiaChiId], [DiaChiChinhXac], [Email], [Website], [Rank]) VALUES (2, N'Nước     ', 1, N'123 Lý Thường Kiệt , P10, Q10 ', N'fff@gmail.com', N'www.ffff.com', 2)
INSERT [dbo].[tbl_CongTy] ([Id], [Ten], [DiaChiId], [DiaChiChinhXac], [Email], [Website], [Rank]) VALUES (3, N'Sách     ', 2, N'333 Lý Thường Kiệt , P3, Q3', NULL, NULL, NULL)
INSERT [dbo].[tbl_CongTy] ([Id], [Ten], [DiaChiId], [DiaChiChinhXac], [Email], [Website], [Rank]) VALUES (4, N'Computer  ', 2, N'333 Lý Thường Kiệt , P3, Q3', NULL, NULL, NULL)
INSERT [dbo].[tbl_CongTy] ([Id], [Ten], [DiaChiId], [DiaChiChinhXac], [Email], [Website], [Rank]) VALUES (5, N'Bánh     ', 3, N'444 Trường Chinh , P5, Q5', NULL, NULL, NULL)
INSERT [dbo].[tbl_CongTy] ([Id], [Ten], [DiaChiId], [DiaChiChinhXac], [Email], [Website], [Rank]) VALUES (6, N'Keo       ', 4, N'555 Trường Chinh', NULL, NULL, NULL)
SET IDENTITY_INSERT [dbo].[tbl_CongTy] OFF
/****** Object:  Table [dbo].[tbl_CongTy_NganhNghe]    Script Date: 05/30/2012 08:52:03 ******/
SET IDENTITY_INSERT [dbo].[tbl_CongTy_NganhNghe] ON
INSERT [dbo].[tbl_CongTy_NganhNghe] ([Id], [CongTyId], [NganhNgheId]) VALUES (1, 2, 1)
INSERT [dbo].[tbl_CongTy_NganhNghe] ([Id], [CongTyId], [NganhNgheId]) VALUES (2, 2, 2)
INSERT [dbo].[tbl_CongTy_NganhNghe] ([Id], [CongTyId], [NganhNgheId]) VALUES (3, 3, 1)
SET IDENTITY_INSERT [dbo].[tbl_CongTy_NganhNghe] OFF
/****** Object:  Table [dbo].[tbl_CongTy_Fax]    Script Date: 05/30/2012 08:52:03 ******/
SET IDENTITY_INSERT [dbo].[tbl_CongTy_Fax] ON
INSERT [dbo].[tbl_CongTy_Fax] ([Id], [SoFax], [CongTyId]) VALUES (1, N'1212121212', 2)
INSERT [dbo].[tbl_CongTy_Fax] ([Id], [SoFax], [CongTyId]) VALUES (2, N'30321512121', 3)
INSERT [dbo].[tbl_CongTy_Fax] ([Id], [SoFax], [CongTyId]) VALUES (3, N'657568678', 3)
SET IDENTITY_INSERT [dbo].[tbl_CongTy_Fax] OFF
/****** Object:  Table [dbo].[tbl_CongTy_DienThoai]    Script Date: 05/30/2012 08:52:03 ******/
SET IDENTITY_INSERT [dbo].[tbl_CongTy_DienThoai] ON
INSERT [dbo].[tbl_CongTy_DienThoai] ([Id], [SoDienThoai], [CongTyId]) VALUES (1, N'09565656', 2)
INSERT [dbo].[tbl_CongTy_DienThoai] ([Id], [SoDienThoai], [CongTyId]) VALUES (10, N'89789', 3)
INSERT [dbo].[tbl_CongTy_DienThoai] ([Id], [SoDienThoai], [CongTyId]) VALUES (13, N'77768678', 2)
SET IDENTITY_INSERT [dbo].[tbl_CongTy_DienThoai] OFF
