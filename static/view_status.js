function init() {

    var $ = go.GraphObject.make;  // for conciseness in defining templates

    myDiagram = $(go.Diagram, "status",  // create a Diagram for the DIV HTML element
        {
            initialContentAlignment: go.Spot.Center,  // center the content
            "undoManager.isEnabled": true  // enable undo & redo
        });

    // define a simple Node template
    myDiagram.nodeTemplate =
        $(go.Node, "Auto",  // the Shape will go around the TextBlock
            $(go.Shape, "RoundedRectangle", { strokeWidth: 0},
                // Shape.fill is bound to Node.data.color
                new go.Binding("fill", "color")),
            $(go.TextBlock,
                { margin: 8 },  // some room around the text
                // TextBlock.text is bound to Node.data.key
                new go.Binding("text", "key"))
        );

    // but use the default Link template, by not setting Diagram.linkTemplate

    // create the model data that will be represented by Nodes and Links
    myDiagram.model = new go.GraphLinksModel(
        [
            { key: "Resume Submitted", color: "lightgreen" },
            { key: "1st Technical Phone Interview", color: "lightgreen" },
            { key: "2nd Technical Phone Interview", color: "lightgreen" },
            { key: "Hiring Committee Review", color: "red" },
            { key: "Offer Stage", color: "white" }
        ],
        [
            { from: "Resume Submitted", to: "1st Technical Phone Interview" },
            { from: "1st Technical Phone Interview", to: "2nd Technical Phone Interview" },
            { from: "2nd Technical Phone Interview", to: "Hiring Committee Review" },
            { from: "Hiring Committee Review", to: "Offer Stage" }
        ]);
}
$(function() {
    $("#job-list").empty();
    $.ajax({
        url: "/interview/status",
        type: "GET",
        success: function(data) {
            data = data["interviews"];
            for (var i in data) {
                var job = data[i];
                console.log(job);
                $("#job-list").append($("<option></option>").html(job["job_title"]));
            }
        }
    });
    init();
});