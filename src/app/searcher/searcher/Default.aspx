<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.master" AutoEventWireup="true" CodeBehind="~/Default.aspx.cs" CodeFile="~/Default.aspx.cs" Inherits="searcher._Default" %>
<%@ Register assembly="AjaxControlToolkit" namespace="AjaxControlToolkit" tagprefix="asp" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="HeadContent">
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="MainContent">
    <asp:Label ID="lblTest" style="display:none;" runat="server"></asp:Label>
    <div class="container">
        <div class="sidebar">
            <div class="searchBox">
                    <asp:TextBox ID="txtsName" Width="60%" runat="server" Text="Nhập thông tin tìm kiếm.."></asp:TextBox>
                    <asp:Button ID="btnsSubmit" runat="server" Text="Search" 
                        onclick="btnsSubmit_Click"  OnClientClick="resultLoad();"/>
            </div>
            Kết quả tìm kiếm:
            <%--<asp:ScriptManager ID="ScriptManager1" runat="server">
            <CompositeScript>
                <Scripts>
                    <asp:ScriptReference Path="~/Scripts/main.js" />
                </Scripts>
            </CompositeScript>
            </asp:ScriptManager>--%>
            <div class="resultBox">
                <%--<asp:UpdatePanel ID="UpdatePanel1" UpdateMode="Conditional" runat="server">
                <ContentTemplate>--%>
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
                <%--</ContentTemplate>
                <Triggers>
                    <asp:AsyncPostBackTrigger ControlID="btnsSubmit" EventName="Click"/>
                </Triggers>
                </asp:UpdatePanel>--%>
            </div> 
                    
        
        </div>
        <div class="map" id="map_canvas"></div>
        <div class="toolbox">Xem toàn màn hình</div>
    </div>
</asp:Content>
