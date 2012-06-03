using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data.SqlClient;
using System.Data;
using Newtonsoft.Json;

namespace searcher
{
    public partial class _Default : System.Web.UI.Page
    {
        static string[] items;
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                string sql = "SELECT TOP (100) DuongKhongDau , MAX(RankDC) AS Expr1 " +
                                " FROM tbl_DiaChi " +
                                " GROUP BY DuongKhongDau " +
                                " ORDER BY expr1 DESC";
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
                string updateRankDC = "";
                whereclause = "WHERE DuongKhongDau LIKE N'%" + txtsName.Text.Trim().Replace(",", "") + "%'";
                whereclause2 = " OR Ten LIKE N'%" + txtsName.Text.Trim().Replace(",", "") + "%'";
                if (IsNumber(chitiet[0].ToString()))
                {
                    diachi = txtsName.Text.Trim().Replace(",", "").Split(new char[] { ' ' }, 2);
                    if (diachi.Length == 2)
                        whereclause += " OR (SoNha LIKE '%" + diachi[0] + "%' AND DuongKhongDau LIKE N'%" + diachi[1] + "%')";
                }
                if (whereclause != "")
                {
                    string query = "SELECT * FROM SEARCH_DIACHI_VW " + whereclause + whereclause2;
                    updateRankDC = "UPDATE tbl_DiaChi SET RankDC +=1 " + whereclause;
                    Database.ExecuteNonQuery(updateRankDC);
                    DataTable dt = Database.GetData(query);
                    dlResult.DataSource = dt;
                    dlResult.DataBind();
                }
                else
                {
                    dlResult.DataSource = null;
                    dlResult.DataBind();
                    //Response.Redirect(Request.Url.ToString());
                }

            }
            //btnsSubmit.Attributes.Add("onclick", "javascript:resultLoad();");
        }

        [System.Web.Services.WebMethodAttribute(), System.Web.Script.Services.ScriptMethodAttribute()]
        static bool IsNumber(string value)
        {
            // Return true if this is a number.
            int number1;
            return int.TryParse(value, out number1);
        }
    }
}
