<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.master" AutoEventWireup="true" CodeBehind="~/Default.aspx.cs" CodeFile="~/Default.aspx.cs" Inherits="searcher._Default" %>
<%@ Register assembly="AjaxControlToolkit" namespace="AjaxControlToolkit" tagprefix="asp" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="HeadContent">
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="MainContent">
    <div class="container">
        <div class="sidebar">
            <div class="searchBox">
                    <asp:TextBox ID="txtsName" runat="server"></asp:TextBox>
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
                <asp:DataList ID="dlResult" runat="server" Width="100%">
                    <ItemTemplate>
                        <div class="result">
                            <div class="rName"><asp:Label ID="lblName" runat="server"  Text='<%# Eval("Ten") %>'></asp:Label><br/></div>
                            <div class="rAddr"><asp:Label ID="lblAddr" runat="server"  Text='<%# Eval("DiaChiChinhXac") %>'></asp:Label></div>
                            <div class="rPhone">0168.991.7713</div>
                            <div class="rDetail"></div>
                        </div>
                    </ItemTemplate>
                </asp:DataList>
                                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
                 <div class="result">
                    <div class="rName">10. Tên công  ty</div>
                    <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div>
                    <div class="rPhone">0168.991.7713</div>
                    <div class="rLocation">10.759734,106.661321</div>
                    <div class="rDetail"></div>
                    <!-- display none -->
                    <div class="rFax">0168.991.7713</div>
                    <div class="rEmail">hungvinhbk@gmail.com</div>
                    <div class="rWebsite">http://hungvjnh.com</div>
                    <div class="rBiz">Công nghệ thông tin</div>
                </div>
            </div>
            <div id="infowindow">
                <div id="icontent">
                <div class="rName">10. Tên công  ty</div><br />
                - Địa chỉ: <div class="rAddr">497 Hòa Hảo, P7, Q10, Tp. HCM</div><br />
                - Số điện thoại: <div class="rPhone">0168.991.7713</div><br />
                - Fax: <div class="rFax">0168.991.7713</div><br />
                - Email: <div class="rEmail">hungvinhbk@gmail.com</div><br />
                - Website: <div class="rWebsite">http://hungvjnh.com</div><br />
                - Lĩnh vực kinh doanh: <div class="rBiz">Công nghệ thông tin</div><br />
                </div>
            </div>
            Trang <1> <2>
        </div>
        <div class="map" id="map_canvas">
        
        </div>
    </div>
    

</asp:Content>
