<%@ Page Title="BanDo24h.com" Language="C#" MasterPageFile="~/MasterPage.master" AutoEventWireup="true" CodeFile="Default.aspx.cs" Inherits="_Default" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="head">
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="MainContent">
<script type="text/javascript">
    var prm = Sys.WebForms.PageRequestManager.getInstance();
    prm.add_endRequest(resultLoad);
</script>
    <asp:Label ID="lblTest" style="display:none;" runat="server"></asp:Label>
    <div class="container">
        <div class="sidebar">
            <div class="searchBox">
                    <asp:TextBox class="textbox" ID="txtsName" Width="280px" runat="server" Text="Nhập thông tin tìm kiếm.."></asp:TextBox>
                    <asp:Button ID="btnsSubmit" runat="server" Text="Tìm kiếm" 
                        onclick="btnsSubmit_Click" BackColor="#99CCFF" Font-Bold="False" 
                        Font-Italic="False" />
            </div>
            Kết quả tìm kiếm:
            <asp:ScriptManager ID="ScriptManager1" runat="server" EnablePartialRendering="True">
            <CompositeScript>
                <Scripts>
                    <%--<asp:ScriptReference Path="~/Scripts/main.js" />--%>
                </Scripts>
            </CompositeScript>
            </asp:ScriptManager>
            <asp:UpdatePanel ID="UpdatePanel1" UpdateMode="Conditional" runat="server">
                <ContentTemplate>
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
                                                    - Số điện thoại: <div class="rPhone"><asp:Label ID="lblIPhone" runat="server" Text='<%# (String.IsNullOrEmpty(Eval("SoDienThoai").ToString()) ? "---" : Eval("SoDienThoai").ToString().Replace(","," - ")) %>'></asp:Label></div><br />
                                                    - Fax: <div class="rFax"><asp:Label ID="lblIFax" runat="server" Text='<%# (String.IsNullOrEmpty(Eval("SoFax").ToString()) ? "---" : Eval("SoFax").ToString().Replace(","," - ")) %>'></asp:Label></div><br />
                                                    - Email: <div class="rEmail"><asp:Label ID="lblIEmail" runat="server" Text='<%# (String.IsNullOrEmpty(Eval("Email").ToString()) ? "---" : Eval("Email")) %>'></asp:Label></div><br />
                                                    - Website: <div class="rWebsite"><asp:Label ID="lblIWebsite" runat="server" Text='<%# (String.IsNullOrEmpty(Eval("Website").ToString()) ? "---" : Eval("Website")) %>'></asp:Label></div><br />
                                                    - Lĩnh vực kinh doanh: <div class="rBiz"><asp:Label ID="lblILinhVuc" runat="server" Text='<%# Eval("NganhNghe").ToString().Replace(","," - ") %>'></asp:Label></div><br />
                                                </div>
                                            </div>
                                        </div>
                                    </ItemTemplate>
                                </asp:DataList> 
                
                    </div> 
                    <table>
                    <tr>
                    <td colspan="5">  </td>
                    </tr>
                    <tr>
                    <td width="80" valign="top" align="center"><asp:LinkButton ID="lnkFirst" 
                            runat="server" onclick="lnkFirst_Click">First</asp:LinkButton></td>
                    <td width="80" valign="top" align="center"><asp:LinkButton ID="lnkPrevious" 
                            runat="server" onclick="lnkPrevious_Click">Previous</asp:LinkButton></td>
                    <td>
                            <asp:DataList ID="DataListPaging" runat="server" RepeatDirection="Horizontal" 
                                onitemcommand="DataListPaging_ItemCommand" 
                                onitemdatabound="DataListPaging_ItemDataBound">
                            <ItemTemplate>
                                <asp:LinkButton ID="Pagingbtn" runat="server" CommandArgument='<%# Eval("PageIndex") %>' CommandName="newpage" Text='<%# Eval("PageText") %> '></asp:LinkButton> 
                            </ItemTemplate>
                            </asp:DataList> 
                    </td>
                    <td width="80" valign="top" align="center">
                            <asp:LinkButton ID="lnkNext" runat="server" onclick="lnkNext_Click">Next</asp:LinkButton>
                    </td>
                    <td width="80" valign="top" align="center">
                        <asp:LinkButton ID="lnkLast" runat="server" onclick="lnkLast_Click">Last</asp:LinkButton>
                    </td>
                    </tr> 
                    </table> 
                    <asp:Label ID="lblpage" runat="server" Text=""></asp:Label>
                </ContentTemplate>
                <Triggers>
                    <asp:AsyncPostBackTrigger ControlID="btnsSubmit" EventName="Click"/>
                </Triggers>
           </asp:UpdatePanel>
            <asp:UpdateProgress ID="UpdateProgress1" runat="server">
            <ProgressTemplate>
                   <div id="loading" class="progress">   
                        <img src="Styles/images/processing.gif" />
                   </div>
                </ProgressTemplate>
            </asp:UpdateProgress>
    
        </div>
        <div class="map" id="map_canvas"></div>
        <div class="toolbox">Xem toàn màn hình</div>
    </div>
</asp:Content>

