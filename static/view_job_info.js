// var job_list = [{job: "Development Engineer", desc:"Develope Product"},
//             {job:"Test Engineer", desc:"Test Function"},
//             {job:"Algorithm Engineer", desc:"Design Algorithm"}];
//
// window.onload = function(){
//       var tbody = document.getElementById('tb_job_info');
//
//       for(var i = 0;i < job_list.length; i++){ //遍历一下json数据
//           var trow = getDataRow(per[i]); //定义一个方法,返回tr数据
//           tbody.appendChild(trow);
//       }
// }
//
// function getDataRow(h){
//  var row = document.createElement('tr'); //创建行
//
//  var jobCell = document.createElement('td'); //创建第一列job
//  jobCell.innerHTML = h.job; //填充数据
//  row.appendChild(jobCell); //加入行  ，下面类似
//
//  var descCell = document.createElement('td');//创建第二列desc
//  descCell.innerHTML = h.desc;
//  row.appendChild(descCell);
//
//  return row; //返回tr数据
// }
//---------------------以上copy/paste---------------------
$(function() {
    $.ajax({
        //--------注意：url要改为测试，最后要改为接口中定义的--------------
        url: "/view_job_info",
        type: "GET",

        success: function(data) {
            // 疑点：data[job_list] 还是 data["job_list"]
            var job_list = data["job_list"];
            var tbody = $("tbody_job_info");

            for(var i = 0;i < job_list.length; i++){ //遍历一下json数据
                var trow = getDataRow(job_list[i]); //定义一个方法,返回tr数据
                tbody.appendChild(trow);
            }
        },
        error: function() {
            alert("")
        }
    });
    function getDataRow(h){
        var row = document.createElement('tr'); //创建行

        var jobCell = document.createElement('td'); //创建第一列job
        jobCell.innerHTML = h["job"]; //填充数据
        row.appendChild(jobCell); //加入行  ，下面类似

        var descCell = document.createElement('td');//创建第二列desc
        descCell.innerHTML = h["desc"];
        row.appendChild(descCell);

        return row; //返回tr数据
    }
});