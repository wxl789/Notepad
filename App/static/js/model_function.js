LASTOPTID = "ID_LI_Home";
BASICDIR = "/static/html/";

function change_class(ID) {

    $("#" + ID).click(function () {

        $("#" + LASTOPTID).removeClass("active");

        $("#" + ID).addClass("active");

        LASTOPTID = ID;
    });
}

function backup_data(cmd) {

}
//把button和页面进行绑定,点击不同的button显示不同的页面
function bind_content_page(ID) {

    var click_action = function (ID) {

        param = ID.split('_');

        if (param[1] == "Get") {

            page = "get";

        } else if (param[1] == "Backup") {

            page = "backup";

        } else if (param[1] == "Index") {

            page = "home";

        } else if (param[1] == "Add") {

            page = "add";

        } else if (param[1] == "Change") {

            page = "change";

        }

        $("#content").load(BASICDIR + page + ".html");

    }

    $("#" + ID).click(function () {

        click_action(ID);

    });
}

$(document).ready(function () {

    bind_content_page("ID_Index");
    bind_content_page("ID_Add");
    bind_content_page("ID_Get");
    bind_content_page("ID_Backup");
    bind_content_page("ID_Change_Password");

    // bind_content_page("ID_Get_KaiPiaoRen");
    // bind_content_page("ID_Get_SiJi");
    // bind_content_page("ID_Get_RiQi");
    // bind_content_page("ID_Get_All");
    //
    // bind_content_page("ID_Backup_Current");
    // bind_content_page("ID_Backup_SiJi");
    // bind_content_page("ID_Backup_KaiPiaoRen");


    //选中样式切换
    change_class("ID_LI_Home");
    change_class("ID_LI_Add");
    change_class("ID_LI_Get");
    change_class("ID_LI_Backup");
    change_class("ID_LI_Person");

    //第一次进入首页的时候加载home页面的内容
    $("#content").load(BASICDIR + "home.html");

});