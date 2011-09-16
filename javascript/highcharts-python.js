/*
 * Create a jQuery function that allows us to load a chart
 * based on a server side config in one step.
 * 
 * For example, to load a chart generated at the url /charts/sample with
 * a custom title and render it to the div with id 'banana':
 * 
 *     $('#banana').renderChart('/charts/toomah', {title: {text: 'A Better Title'}})
 *
 * Options that you override are exactly those given in the highcharts documentation at:
 *
 * http://www.highcharts.com/ref/
 */

(function($){
    $.fn.renderChart = function(url, options) {
        objects = this;
        options = options || {};
        $.getJSON(url, {}, function(config) {
            config = $.extend(true, config, options);
            config.chart = config.chart || {};
            $.each(objects.get(), function() {
                config.chart.renderTo = this;
                new Highcharts.Chart(config); 
            });
        });
    };
})(jQuery);
