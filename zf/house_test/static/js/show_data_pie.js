function pie_chart(data) {
    // 初始化一个 Echarts实例
    var myChart = echarts.init(document.getElementById('pie'));

    window.addEventListener('resize', function () {
        myChart.resize();
    });

    var option = {
        tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)",
        },

        series:[{

            name: '户型的占比',

            type: 'pie',

            radius: ['0%', '50%'],
            center: ['50%', '60%'],

            labelLine: {

                normal: {
                    show: true
                },
                // 选中后加重表现
                emphasis: {
                    show: true
                }
            },
            // 饼状图的内部名字
            label: {
                normal: {
                    show: true
                },
                emphasis: {
                    show: true
                }
            },
            //
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            },
            data: data,
        }]
    };

    myChart.setOption(option); // 根据配置项生成图表
}