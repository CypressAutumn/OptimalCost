$(document).ready(function(){
    //添加行
    $('#add-row').on('click', function(){
        $('#spec-container').append(' \
        <div class="input-group mt-2"> \
            <div class="input-group-prepend"> \
            <span class="input-group-text">物料</span> \
        </div> \
        <input type="text" aria-label="First name" class="form-control" placeholder="规格（mm）"> \
        <input type="text" aria-label="Last name" class="form-control" placeholder="价格（x.00）"> \
        </div> \
        ');
    });
    //删除行
    $('#remove-row').on('click', function(){
        var spec_items = $('#spec-container').children();
        var total_items = spec_items.length-1;
        $('#spec-container').children().eq(total_items).remove();
    });
    //计算
    $('#count-rows').on('click', function(){
        var group_json = {}
        var spec_list = []
        var cost_list = []
        $('#spec-container').children().each(function(index){
            var spec = $(this).find('input').eq(0).val();
            var cost = $(this).find('input').eq(1).val();
            spec_list.push(spec);
            cost_list.push(cost);
        });
        group_json.spec = spec_list;
        group_json.cost = cost_list;
        console.log(group_json);
        $.ajax({
            type: "POST",
            url: "/count",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(group_json),
            dataType: "json",
            success: function (message) {
                console.log(message)
            },
            error: function (message) {
                console.log(message)
            }
        });
    })
});

var ctx = document.getElementById('myChart').getContext("2d");

        var gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
        gradientStroke.addColorStop(0, '#00d8c0');
        gradientStroke.addColorStop(1, '#ff6a72');

        var gradientFill = ctx.createLinearGradient(500, 0, 100, 0);
        gradientFill.addColorStop(0, "rgba(0, 216, 192, 0.10)");
        gradientFill.addColorStop(1, "rgba(255, 106, 114, 0.10)");

        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL"],
                datasets: [{
                    label: "Data",
                    borderColor: gradientStroke,
                    pointBorderColor: gradientStroke,
                    pointBackgroundColor: gradientStroke,
                    pointHoverBackgroundColor: gradientStroke,
                    pointHoverBorderColor: gradientStroke,
                    pointBorderWidth: 2,
                    pointHoverRadius: 2,
                    pointHoverBorderWidth: 1,
                    pointRadius: 3,
                    fill: true,
                    backgroundColor: gradientFill,
                    borderWidth: 2,
                    data: [50, 150, 200, 270, 320, 470, 500]
                }]
            },
            options: {
                legend: {
                    position: "bottom"
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            fontColor: "grey",
                            fontStyle: "bold",
                            beginAtZero: true,
                            maxTicksLimit: 5,
                            padding: 20
                        },
                        gridLines: {
                            drawTicks: false,
                            display: false
                        }

                    }],
                    xAxes: [{
                        gridLines: {
                            zeroLineColor: "transparent"
                        },
                        ticks: {
                            padding: 20,
                            fontColor: "grey",
                            fontStyle: "bold"
                        }
                    }]
                }
            }
        });
