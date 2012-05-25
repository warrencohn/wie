using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace searcher
{
    public partial class AjaxHandler : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            Response.Expires = -1;
            //required to keep the page from being cached on the client's browser

            Response.ContentType = "text/plain";
            Response.Write(DateTime.Now.ToString());
            Response.End();
        }
    }
}