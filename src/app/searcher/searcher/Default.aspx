<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.master" AutoEventWireup="true"
    CodeBehind="Default.aspx.cs" Inherits="searcher._Default" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="HeadContent">
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="MainContent">
    <div class="container">
        <div class="sidebar">
            <div class="searchBox">
                    <asp:TextBox ID="sName" runat="server" Text="Nhập thông tin tìm kiếm.."></asp:TextBox>
                    <asp:DropDownList ID="sType" runat="server">
                        <asp:ListItem>Địa chỉ</asp:ListItem>
                        <asp:ListItem>Công ty</asp:ListItem>
                    </asp:DropDownList>

                    <asp:Button ID="sSubmit" runat="server" Text="Search" />
            </div>
            Kết quả tìm kiếm:
            <div class="resultBox">
                <div class="result">
                    <div class="rName">1. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rDetail"></div>
                </div>
                <div class="result">
                    <div class="rName">1. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rDetail"></div>
                </div>
                <div class="result">
                    <div class="rName">1. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rDetail"></div>
                </div>
                <div class="result">
                    <div class="rName">1. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rDetail"></div>
                </div>
                <div class="result">
                    <div class="rName">1. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rDetail"></div>
                </div>
                <div class="result">
                    <div class="rName">1. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rDetail"></div>
                </div>
                <div class="result">
                    <div class="rName">1. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rDetail"></div>
                </div>
                <div class="result">
                    <div class="rName">1. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rDetail"></div>
                </div>
                <div class="result">
                    <div class="rName">1. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rDetail"></div>
                </div>
            </div>
        </div>
        <div class="map" id="map_canvas">
        
        </div>
    </div>
    

</asp:Content>
