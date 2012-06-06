using System;
using System.Data;
using System.Configuration;
using System.Collections;
using System.Web;
using System.Web.Configuration;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.WebControls.WebParts;
using System.Web.UI.HtmlControls;

namespace searcher
{
    public partial class _Default : System.Web.UI.Page
    {
        PagedDataSource pgsource = new PagedDataSource();
        int findex, lindex;
        string query = "";
        static string[] items;
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                dlResult.DataSource = null;
                dlResult.DataBind();
                DataListPaging.DataSource = null;
                DataListPaging.DataBind();
                lnkFirst.Enabled = false;
                lnkLast.Enabled = false;
                lnkNext.Enabled = false;
                lnkPrevious.Enabled = false;
                string sql = "SELECT TenKhongDau FROM tbl_ConDuong";
                DataTable dt = Database.GetData(sql);
                items = new string[dt.Rows.Count];
                int i = 0;
                foreach (DataRow dr in dt.Rows)
                {
                    items.SetValue(dr[0].ToString(), i);
                    i++;
                }
                for (int index = 0; index < items.Length; index++)
                    lblTest.Text += items[index] + (index == items.Length - 1 ? "" : "|");

            }


        }
        protected void btnsSubmit_Click(object sender, EventArgs e)
        {
            if (txtsName.Text != "")
            {
                string[] diachi;
                string chitiet = txtsName.Text;
                string whereclause = "";
                string whereclause2 = "";
                //string updateRankDC = "";
                whereclause = "WHERE DuongKhongDau LIKE N'%" + txtsName.Text.Trim().Replace(",", "") + "%'";
                whereclause2 = " OR TenKhongDau LIKE N'%" + txtsName.Text.Trim().Replace(",", "") + "%'";
                if (IsNumber(chitiet[0].ToString()))
                {
                    diachi = txtsName.Text.Trim().Replace(",", "").Split(new char[] { ' ' }, 2);
                    if (diachi.Length == 2)
                        whereclause += " OR (SoNha LIKE '%" + diachi[0] + "%' AND DuongKhongDau LIKE N'%" + diachi[1] + "%')";
                }

                query = "SELECT * FROM vw_CongTy " + whereclause + whereclause2;
                //updateRankDC = "UPDATE tbl_DiaChi SET RankDC +=1 " + whereclause;
                //Database.ExecuteNonQuery(updateRankDC);
                ViewState["query"] = query;
                //DataTable dt = Database.GetData(query);
                //dlResult.DataSource = dt;
                //dlResult.DataBind();
                BindDataList();
            }
            else
            {
                ViewState["query"] = "";
                dlResult.DataSource = null;
                dlResult.DataBind();
                DataListPaging.DataSource = null;
                DataListPaging.DataBind();
                lnkFirst.Enabled = false;
                lnkLast.Enabled = false;
                lnkNext.Enabled = false;
                lnkPrevious.Enabled = false;

            }
        }

        [System.Web.Services.WebMethodAttribute(), System.Web.Script.Services.ScriptMethodAttribute()]
        static bool IsNumber(string value)
        {
            int number1;
            return int.TryParse(value, out number1);
        }
        private void BindDataList()
        {
            //Create new DataTable dt
            string str = ViewState["query"].ToString();
            DataTable dt = Database.GetData(str);
            pgsource.DataSource = dt.DefaultView;

            //Set PageDataSource paging 
            pgsource.AllowPaging = true;

            //Set number of items to be displayed in the DataList using drop down list
            //if (ddlIndex.SelectedIndex == -1 || ddlIndex.SelectedIndex == 0)
            //{
            //    pgsource.PageSize = 10;
            //}
            //else
            //{
            //    pgsource.PageSize = Convert.ToInt32(ddlIndex.SelectedItem.Value);
            //}
            pgsource.PageSize = 10;


            //Get Current Page Index
            pgsource.CurrentPageIndex = CurrentPage;

            //Store it Total pages value in View state
            ViewState["totpage"] = pgsource.PageCount;

            //Below line is used to show page number based on selection like "Page 1 of 20"
            lblpage.Text = "Page " + (CurrentPage + 1) + " of " + pgsource.PageCount;

            //Enabled true Link button previous when current page is not equal first page 
            //Enabled false Link button previous when current page is first page
            lnkPrevious.Enabled = !pgsource.IsFirstPage;

            //Enabled true Link button Next when current page is not equal last page 
            //Enabled false Link button Next when current page is last page
            lnkNext.Enabled = !pgsource.IsLastPage;

            //Enabled true Link button First when current page is not equal first page 
            //Enabled false Link button First when current page is first page
            lnkFirst.Enabled = !pgsource.IsFirstPage;

            //Enabled true Link button Last when current page is not equal last page 
            //Enabled false Link button Last when current page is last page
            lnkLast.Enabled = !pgsource.IsLastPage;

            //Bind resulted PageSource into the DataList
            dlResult.DataSource = pgsource;
            dlResult.DataBind();

            //Create Paging in the second DataList "DataListPaging"
            doPaging();
        }
        private void doPaging()
        {
            DataTable dt = new DataTable();
            //Add two column into the DataTable "dt" 
            //First Column store page index default it start from "0"
            //Second Column store page index default it start from "1"
            dt.Columns.Add("PageIndex");
            dt.Columns.Add("PageText");

            //Assign First Index starts from which number in paging data list
            findex = CurrentPage - 5;

            //Set Last index value if current page less than 5 then last index added "5" values to the Current page else it set "10" for last page number
            if (CurrentPage > 5)
            {
                lindex = CurrentPage + 5;
            }
            else
            {
                lindex = 10;
            }

            //Check last page is greater than total page then reduced it to total no. of page is last index
            if (lindex > Convert.ToInt32(ViewState["totpage"]))
            {
                lindex = Convert.ToInt32(ViewState["totpage"]);
                findex = lindex - 10;
            }

            if (findex < 0)
            {
                findex = 0;
            }

            //Now creating page number based on above first and last page index
            for (int i = findex; i < lindex; i++)
            {
                DataRow dr = dt.NewRow();
                dr[0] = i;
                dr[1] = i + 1;
                dt.Rows.Add(dr);
            }

            //Finally bind it page numbers in to the Paging DataList
            DataListPaging.DataSource = dt;
            DataListPaging.DataBind();
        }
        private int CurrentPage
        {
            get
            {   //Check view state is null if null then return current index value as "0" else return specific page viewstate value
                if (ViewState["CurrentPage"] == null)
                {
                    return 0;
                }
                else
                {
                    return ((int)ViewState["CurrentPage"]);
                }
            }
            set
            {
                //Set View statevalue when page is changed through Paging DataList
                ViewState["CurrentPage"] = value;
            }
        }
        protected void DataListPaging_ItemCommand(object source, DataListCommandEventArgs e)
        {
            if (e.CommandName.Equals("newpage"))
            {
                //Assign CurrentPage number when user click on the page number in the Paging DataList
                CurrentPage = Convert.ToInt32(e.CommandArgument.ToString());
                //Refresh DataList "DlistEmp" Data once user change page
                BindDataList();
            }
        }
        protected void lnkFirst_Click(object sender, EventArgs e)
        {
            //If user click First Link button assign current index as Zero "0" then refresh DataList "DlistEmp" Data.
            CurrentPage = 0;
            BindDataList();
        }

        protected void lnkLast_Click(object sender, EventArgs e)
        {
            //If user click Last Link button assign current index as totalpage then refresh DataList "DlistEmp" Data.
            CurrentPage = (Convert.ToInt32(ViewState["totpage"]) - 1);
            BindDataList();
        }

        protected void lnkPrevious_Click(object sender, EventArgs e)
        {
            //If user click Previous Link button assign current index as -1 it reduce existing page index.
            CurrentPage -= 1;
            //refresh DataList "DlistEmp" Data
            BindDataList();
        }

        protected void lnkNext_Click(object sender, EventArgs e)
        {
            //If user click Next Link button assign current index as +1 it add one value to existing page index.
            CurrentPage += 1;

            //refresh DataList "DlistEmp" Data
            BindDataList();
        }
        protected void DataListPaging_ItemDataBound(object sender, DataListItemEventArgs e)
        {
            //Enabled False for current selected Page index
            LinkButton lnkPage = (LinkButton)e.Item.FindControl("Pagingbtn");
            if (lnkPage.CommandArgument.ToString() == CurrentPage.ToString())
            {
                lnkPage.Enabled = false;
            }
        }
    }
}
