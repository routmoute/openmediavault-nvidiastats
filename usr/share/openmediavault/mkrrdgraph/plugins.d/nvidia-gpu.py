# -*- coding: utf-8 -*-
import openmediavault.mkrrdgraph


class Plugin(openmediavault.mkrrdgraph.IPlugin):
    def create_graph(self, config):
        # Colors
        config.update({
            'title_gpu_utilization': 'GPU Utilization',
            'color_gpu_util': '#5dacdf',
            'title_gpu_memory': 'GPU Memory Usage',
            'color_gpu_mem': '#ff3b30',
            'title_gpu_temperature': 'GPU Temperature',
            'color_gpu_temp': '#ff9500',
            'title_gpu_power': 'GPU Power',
            'color_gpu_power': '#4cd964',
        })

        # GPU Utilization Graph
        args = []
        args.append('{image_dir}/nvidia-gpu-0-utilization-{period}.png'.format(**config))
        args.extend(config['defaults'])
        args.extend(['--start', config['start']])
        args.extend(['--title', '"{title_gpu_utilization}{title_by_period}"'.format(**config)])
        args.append('--slope-mode')
        args.extend(['--upper-limit', '100'])
        args.extend(['--lower-limit', '0'])
        args.append('--rigid')
        args.extend(['--vertical-label', 'Percent'])
        args.append('DEF:util={data_dir}/nvidia-gpu-0/gauge-utilization.rrd:value:AVERAGE'.format(**config))
        args.append('AREA:util{color_gpu_util}:"GPU Utilization"'.format(**config))
        args.append('LINE1:util#000000')
        args.append('GPRINT:util:LAST:"Current\\: %3.0lf%%"')
        args.append('GPRINT:util:AVERAGE:"Average\\: %3.0lf%%"')
        args.append('GPRINT:util:MAX:"Max\\: %3.0lf%%\\c"')
        args.append('COMMENT:"\\c"')
        args.append('COMMENT:"{last_update}"'.format(**config))
        openmediavault.mkrrdgraph.call_rrdtool_graph(args)

        # GPU Memory Graph
        args = []
        args.append('{image_dir}/nvidia-gpu-0-memory-{period}.png'.format(**config))
        args.extend(config['defaults'])
        args.extend(['--start', config['start']])
        args.extend(['--title', '"{title_gpu_memory}{title_by_period}"'.format(**config)])
        args.append('--slope-mode')
        args.extend(['--vertical-label', 'MiB'])
        args.append('DEF:mem_used={data_dir}/nvidia-gpu-0/gauge-memory_used.rrd:value:AVERAGE'.format(**config))
        args.append('DEF:mem_total={data_dir}/nvidia-gpu-0/gauge-memory_total.rrd:value:AVERAGE'.format(**config))
        args.append('AREA:mem_total#d3d3d3:"Memory Total"')
        args.append('AREA:mem_used{color_gpu_mem}:"Memory Used"'.format(**config))
        args.append('LINE1:mem_total#000000')
        args.append('LINE1:mem_used#000000')
        args.append('GPRINT:mem_used:LAST:"Used (Now)\\: %5.0lfMiB"')
        args.append('GPRINT:mem_total:LAST:"Total\\: %5.0lfMiB\\c"')
        args.append('GPRINT:mem_used:AVERAGE:"Used (Avg)\\: %5.0lfMiB"')
        args.append('GPRINT:mem_used:MAX:"Max\\: %5.0lfMiB\\c"')
        args.append('COMMENT:"\\c"')
        args.append('COMMENT:"{last_update}"'.format(**config))
        openmediavault.mkrrdgraph.call_rrdtool_graph(args)

        # GPU Temperature Graph
        args = []
        args.append('{image_dir}/nvidia-gpu-0-temperature-{period}.png'.format(**config))
        args.extend(config['defaults'])
        args.extend(['--start', config['start']])
        args.extend(['--title', '"{title_gpu_temperature}{title_by_period}"'.format(**config)])
        args.append('--slope-mode')
        args.extend(['--upper-limit', '150'])
        args.extend(['--lower-limit', '0'])
        args.append('--rigid')
        args.extend(['--vertical-label', 'Celsius'])
        args.append('DEF:temp={data_dir}/nvidia-gpu-0/gauge-temperature.rrd:value:AVERAGE'.format(**config))
        args.append('AREA:temp{color_gpu_temp}:"Temperature"'.format(**config))
        args.append('LINE1:temp#000000')
        args.append('GPRINT:temp:LAST:"Current\\: %3.1lf°C"')
        args.append('GPRINT:temp:AVERAGE:"Average\\: %3.1lf°C"')
        args.append('GPRINT:temp:MAX:"Max\\: %3.1lf°C\\c"')
        args.append('COMMENT:"\\c"')
        args.append('COMMENT:"{last_update}"'.format(**config))
        openmediavault.mkrrdgraph.call_rrdtool_graph(args)

        # GPU Power Graph
        args = []
        args.append('{image_dir}/nvidia-gpu-0-power-{period}.png'.format(**config))
        args.extend(config['defaults'])
        args.extend(['--start', config['start']])
        args.extend(['--title', '"{title_gpu_power}{title_by_period}"'.format(**config)])
        args.append('--slope-mode')
        args.extend(['--vertical-label', 'Watts'])
        args.append('DEF:power={data_dir}/nvidia-gpu-0/gauge-power.rrd:value:AVERAGE'.format(**config))
        args.append('DEF:power_limit={data_dir}/nvidia-gpu-0/gauge-power_limit.rrd:value:AVERAGE'.format(**config))
        args.append('AREA:power_limit#d3d3d3:"Limit"')
        args.append('AREA:power{color_gpu_power}:"Power"'.format(**config))
        args.append('LINE1:power_limit#000000')
        args.append('LINE1:power#000000')
        args.append('GPRINT:power:LAST:"Now\\: %3.1lfW"')
        args.append('GPRINT:power_limit:LAST:"Limit\\: %3.1lfW\\c"')
        args.append('GPRINT:power:AVERAGE:"Avg\\: %3.1lfW"')
        args.append('GPRINT:power:MAX:"Max\\: %3.1lfW\\c"')
        args.append('COMMENT:"\\c"')
        args.append('COMMENT:"{last_update}"'.format(**config))
        openmediavault.mkrrdgraph.call_rrdtool_graph(args)

        return 0
