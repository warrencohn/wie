USE [BDSG]
GO
/****** Object:  Table [dbo].[tbl_DiaChi]    Script Date: 05/27/2012 14:06:02 ******/
SET IDENTITY_INSERT [dbo].[tbl_DiaChi] ON
INSERT [dbo].[tbl_DiaChi] ([Id], [SoNha], [Duong], [Phuong], [Quan], [DuongKhongDau], [QuanKhongDau], [IDConDuong], [IDQuan], [IDNha], [BangNha], [X], [Y]) VALUES (1, N'123', N'Lý Thường Kiệt', N'10', N'10', N'Ly Thuong Kiet', N'10', N'LTK100001', N'10100001', 123100001, NULL, NULL, NULL)
INSERT [dbo].[tbl_DiaChi] ([Id], [SoNha], [Duong], [Phuong], [Quan], [DuongKhongDau], [QuanKhongDau], [IDConDuong], [IDQuan], [IDNha], [BangNha], [X], [Y]) VALUES (2, N'333', N'Lý Thường Kiệt', N'7', N'7', N'Ly Thuong Kiet', N'10', N'LTK100001', N'10100001', 123100001, NULL, NULL, NULL)
INSERT [dbo].[tbl_DiaChi] ([Id], [SoNha], [Duong], [Phuong], [Quan], [DuongKhongDau], [QuanKhongDau], [IDConDuong], [IDQuan], [IDNha], [BangNha], [X], [Y]) VALUES (3, N'444', N'Trường Chinh', N'4', N'4', N'Truong Chinh', N'5', NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[tbl_DiaChi] ([Id], [SoNha], [Duong], [Phuong], [Quan], [DuongKhongDau], [QuanKhongDau], [IDConDuong], [IDQuan], [IDNha], [BangNha], [X], [Y]) VALUES (4, N'555', N'Trường Chinh', N'5', N'5', N'Truong Chinh', N'5', NULL, NULL, NULL, NULL, NULL, NULL)
SET IDENTITY_INSERT [dbo].[tbl_DiaChi] OFF
/****** Object:  Table [dbo].[tbl_CongTy]    Script Date: 05/27/2012 14:06:02 ******/
SET IDENTITY_INSERT [dbo].[tbl_CongTy] ON
INSERT [dbo].[tbl_CongTy] ([Id], [Ten], [DiaChiId], [DiaChiChinhXac], [Email], [Website], [Rank]) VALUES (2, N'Nước     ', 1, N'123 Lý Thường Kiệt , P10, Q10 ', N'fff@gmail.com', N'www.ffff.com', 2)
INSERT [dbo].[tbl_CongTy] ([Id], [Ten], [DiaChiId], [DiaChiChinhXac], [Email], [Website], [Rank]) VALUES (3, N'Sách     ', 2, N'333 Lý Thường Kiệt , P3, Q3', NULL, NULL, NULL)
INSERT [dbo].[tbl_CongTy] ([Id], [Ten], [DiaChiId], [DiaChiChinhXac], [Email], [Website], [Rank]) VALUES (4, N'Computer  ', 2, N'333 Lý Thường Kiệt , P3, Q3', NULL, NULL, NULL)
INSERT [dbo].[tbl_CongTy] ([Id], [Ten], [DiaChiId], [DiaChiChinhXac], [Email], [Website], [Rank]) VALUES (5, N'Bánh     ', 3, N'444 Trường Chinh , P5, Q5', NULL, NULL, NULL)
INSERT [dbo].[tbl_CongTy] ([Id], [Ten], [DiaChiId], [DiaChiChinhXac], [Email], [Website], [Rank]) VALUES (6, N'Keo       ', 4, N'555 Trường Chinh', NULL, NULL, NULL)
SET IDENTITY_INSERT [dbo].[tbl_CongTy] OFF
/****** Object:  Table [dbo].[tbl_CongTy_DienThoai]    Script Date: 05/27/2012 14:06:02 ******/
SET IDENTITY_INSERT [dbo].[tbl_CongTy_DienThoai] ON
INSERT [dbo].[tbl_CongTy_DienThoai] ([Id], [SoDienThoai], [CongTyId]) VALUES (1, N'09565656', 2)
INSERT [dbo].[tbl_CongTy_DienThoai] ([Id], [SoDienThoai], [CongTyId]) VALUES (10, N'89789', 3)
INSERT [dbo].[tbl_CongTy_DienThoai] ([Id], [SoDienThoai], [CongTyId]) VALUES (13, N'77768678', 2)
SET IDENTITY_INSERT [dbo].[tbl_CongTy_DienThoai] OFF
