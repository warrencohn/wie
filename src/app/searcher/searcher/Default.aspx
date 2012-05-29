<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.master" AutoEventWireup="true" CodeBehind="~/Default.aspx.cs" CodeFile="~/Default.aspx.cs" Inherits="searcher._Default" %>
<%@ Register assembly="AjaxControlToolkit" namespace="AjaxControlToolkit" tagprefix="asp" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="HeadContent">
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="MainContent">
    <div class="container">
        <div class="sidebar">
            <div class="searchBox">
                    <asp:TextBox ID="txtsName" runat="server" Text="Nhập thông tin tìm kiếm.." OnClick="this.value=''"></asp:TextBox>
                    <asp:AutoCompleteExtender ID="txtsName_AutoCompleteExtender" runat="server" 
                        ServiceMethod="GetCompletionList" TargetControlID="txtsName" 
                        UseContextKey="True" CompletionInterval="1" MinimumPrefixLength="1">
                    </asp:AutoCompleteExtender>
                    <asp:DropDownList ID="ddlsType" runat="server">
                        <asp:ListItem>Địa chỉ</asp:ListItem>
                        <asp:ListItem>Công ty</asp:ListItem>
                    </asp:DropDownList>
                    <asp:Button ID="btnsSubmit" runat="server" Text="Search" 
                        onclick="btnsSubmit_Click"/>
                <asp:ToolkitScriptManager ID="ToolkitScriptManager1" runat="server">
                </asp:ToolkitScriptManager>
            </div>
            Kết quả tìm kiếm:
            <div class="resultBox">
                <asp:DataList ID="dlResult" runat="server" Width="100%" >
                    <ItemTemplate>
                        <div class="result">
                            <div class="rName"><%# Container.ItemIndex + 1 %>. <asp:Label ID="lblName" runat="server"  Text='<%# Eval("Ten") %>'></asp:Label><br/></div>
                            <div><asp:Label ID="lblAddr" class="rAddr" runat="server"  Text='<%# Eval("DiaChiChinhXac") %>'></asp:Label></div>
                            <div class="rDetail"></div>
                            <div><asp:Label class="rLocation" ID="lblLocation" runat="server" Text='<%# Eval("X").ToString().Replace(",",".")+","+Eval("Y").ToString().Replace(",",".")%>'></asp:Label></div>
                            <div class="infowindow1">
                            <div class="icontent">
                                <div class="rName"><asp:Label ID="lblIName" runat="server" Text='<%# Eval("Ten") %>' ></asp:Label></div><br />
                                - Địa chỉ: <div class="rAddr"><asp:Label ID="lblIAddr" runat="server" Text='<%# Eval("DiaChiChinhXac") %>'></asp:Label></div><br />
                                - Số điện thoại: <div class="rPhone"><asp:Label ID="lblIPhone" runat="server" Text='<%# Eval("SoDienThoai").ToString().Replace(","," - ") %>'></asp:Label></div><br />
                                - Fax: <div class="rFax"><asp:Label ID="lblIFax" runat="server" Text='<%# Eval("SoFax").ToString().Replace(","," - ") %>'></asp:Label></div><br />
                                - Email: <div class="rEmail"><asp:Label ID="lblIEmail" runat="server" Text='<%# Eval("Email") %>'></asp:Label></div><br />
                                - Website: <div class="rWebsite"><asp:Label ID="lblIWebsite" runat="server" Text='<%# Eval("Website") %>'></asp:Label></div><br />
                                - Lĩnh vực kinh doanh: <div class="rBiz"><asp:Label ID="lblILinhVuc" runat="server" Text='<%# Eval("NganhNghe").ToString().Replace(","," - ") %>'></asp:Label></div><br />
                            </div>
                        </div>
                        </div>
                        
                    </ItemTemplate>
                </asp:DataList>
                <%--<div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">11.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>--%>
            </div>
            Trang <1> <2>
            
        
        </div>
        <div class="map" id="map_canvas">
        
        </div>
    </div>
    

</asp:Content>
