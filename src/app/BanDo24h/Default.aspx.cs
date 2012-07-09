using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data;
using System.Data.SqlClient;
using System.Web.Configuration;

public partial class _Default : System.Web.UI.Page
{
    PagedDataSource pgsource = new PagedDataSource();
    int findex, lindex;
    string query = "";
    static string[] items;
    //static string conStr = WebConfigurationManager.ConnectionStrings["BanDo24h"].ConnectionString;
    static string conStr = "Data Source=(local);Initial Catalog=BDSG;Integrated Security=True";
    SqlConnection conn = new SqlConnection(conStr);
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
            lnkFirst.Visible = false;
            lnkLast.Visible = false;
            lnkNext.Visible = false;
            lnkPrevious.Visible = false;

            string sql = "SELECT TenConDuong FROM ConDuong";
            //DataTable dt = Database.GetData(sql);
            try
            {
                conn.Open();
                SqlDataAdapter da = new SqlDataAdapter(sql, conn);
                DataSet ds = new DataSet();
                da.Fill(ds, "ConDuong");

                DataTable dt = ds.Tables["ConDuong"];

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
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                conn.Close();
            }
        }
    }
    //private string filter()
    //{
    //    string[] diachi;
    //    string chitiet = txtsName.Text;
    //    string whereclause = "";
    //    //string updateRankDC = "";
    //    whereclause = "WHERE Duong LIKE N'%" + txtsName.Text.Trim().Replace(",", "") + "%' " +
    //        " OR Ten LIKE N'%" + txtsName.Text.Trim().Replace(",", "") + "%'";
    //    //whereclause = "WHERE CONTAINS(Duong,N'" + txtsName.Text.Trim().Replace(",", "") + "') " +
    //    //    " OR CONTAINS(Ten,N'" + txtsName.Text.Trim().Replace(",", "") + "')";
    //    if (IsNumber(chitiet[0].ToString()))
    //    {
    //        diachi = txtsName.Text.Trim().Replace(",", "").Split(new char[] { ' ' }, 2);
    //        if (diachi.Length == 2)
    //            whereclause += " OR (SoNha LIKE '%" + diachi[0] + "%' AND Duong LIKE N'%" + diachi[1] + "%')";
    //        //whereclause += " OR (CONTAINS(SoNha,'" + diachi[0] + "') AND CONTAINS(Duong,N'%" + diachi[1] + "%'))";
    //    }
    //    return whereclause;
    //}
    private string filter()
    {
        string[] nhom;
        string dk = txtsName.Text.Trim();
        string whereClause = "";
        if(IsNumber(dk[0].ToString())) 
        {
            if (dk[0].ToString() == "2" || dk[0].ToString() == "3")
            {
                if (dk == "3 Tháng 2" || dk == "30 Tháng 4" || dk == "26 Tháng 3")
                {
                    whereClause = "Duong = N'" + dk + "' ";
                    return whereClause;
                }
            }
            nhom = dk.Split(new char[] { ' ' }, 2);
            if (nhom.Length == 2)
            {
                whereClause = "SoNha LIKE '%" + nhom[0] + "%' AND Duong LIKE N'%" + nhom[1] + "%' ";
            }
            else if(dk.Length > 5)
            {
                whereClause = "SoDienThoai LIKE '%" + dk + "%' ";
            }
        }
        else //Tim Cong Ty, Ten duong bat dau bang chu
        {
            whereClause = "Ten LIKE N'%" + dk + "%' OR Duong LIKE N'%" + dk + "%' ";
        }
        return whereClause;
    }
    protected void btnsSubmit_Click(object sender, EventArgs e)
    {
        if (txtsName.Text.Length  > 4)
        {
            query = "SELECT * FROM vw_CongTy WHERE " + filter();
            //updateRankDC = "UPDATE tbl_DiaChi SET RankDC +=1 " + whereclause;
            //Database.ExecuteNonQuery(updateRankDC);
            ViewState["query"] = query;
            ViewState["CurrentPage"] = 0;
            BindDataList();
        }
        else //alert nothing 
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
    static bool IsNumber(string value)
    {
        int number1;
        return int.TryParse(value, out number1);
    }
    private void BindDataList()
    {
        try
        {
            conn.Open();
            string str = ViewState["query"].ToString();
            SqlDataAdapter da = new SqlDataAdapter(str, conn);
            DataSet ds = new DataSet();
            da.Fill(ds, "CongTy");
            DataTable dt = ds.Tables["CongTy"];
            //DataTable dt = Database.GetData(str);
            pgsource.DataSource = dt.DefaultView;

            pgsource.AllowPaging = true;
            pgsource.PageSize = 10;
            pgsource.CurrentPageIndex = CurrentPage;
            ViewState["totpage"] = pgsource.PageCount;
            lblpage.Text = "Trang " + (CurrentPage + 1) + " / " + pgsource.PageCount;
            lnkFirst.Visible = true;
            lnkLast.Visible = true;
            lnkNext.Visible = true;
            lnkPrevious.Visible = true;
            lnkPrevious.Enabled = !pgsource.IsFirstPage;
            lnkNext.Enabled = !pgsource.IsLastPage;
            lnkFirst.Enabled = !pgsource.IsFirstPage;
            lnkLast.Enabled = !pgsource.IsLastPage;
            dlResult.DataSource = pgsource;
            dlResult.DataBind();
            doPaging();
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
        finally
        {
            conn.Close();
        }
    }
    private void doPaging()
    {
        DataTable dt = new DataTable();
        dt.Columns.Add("PageIndex");
        dt.Columns.Add("PageText");
        findex = CurrentPage - 5;
        if (CurrentPage > 5)
        {
            lindex = CurrentPage + 5;
        }
        else
        {
            lindex = 10;
        }
        if (lindex > Convert.ToInt32(ViewState["totpage"]))
        {
            lindex = Convert.ToInt32(ViewState["totpage"]);
            findex = lindex - 10;
        }

        if (findex < 0)
        {
            findex = 0;
        }
        for (int i = findex; i < lindex; i++)
        {
            DataRow dr = dt.NewRow();
            dr[0] = i;
            dr[1] = i + 1;
            dt.Rows.Add(dr);
        }
        DataListPaging.DataSource = dt;
        DataListPaging.DataBind();
    }
    private int CurrentPage
    {
        get
        {
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
            ViewState["CurrentPage"] = value;
        }
    }
    protected void DataListPaging_ItemCommand(object source, DataListCommandEventArgs e)
    {
        if (e.CommandName.Equals("newpage"))
        {
            CurrentPage = Convert.ToInt32(e.CommandArgument.ToString());
            BindDataList();
        }
    }
    protected void lnkFirst_Click(object sender, EventArgs e)
    {
        CurrentPage = 0;
        BindDataList();
    }
    protected void lnkLast_Click(object sender, EventArgs e)
    {
        CurrentPage = (Convert.ToInt32(ViewState["totpage"]) - 1);
        BindDataList();
    }

    protected void lnkPrevious_Click(object sender, EventArgs e)
    {
        CurrentPage -= 1;
        BindDataList();
    }

    protected void lnkNext_Click(object sender, EventArgs e)
    {
        CurrentPage += 1;
        BindDataList();
    }
    protected void DataListPaging_ItemDataBound(object sender, DataListItemEventArgs e)
    {
        LinkButton lnkPage = (LinkButton)e.Item.FindControl("Pagingbtn");
        if (lnkPage.CommandArgument.ToString() == CurrentPage.ToString())
        {
            lnkPage.Enabled = false;
        }
    }
}