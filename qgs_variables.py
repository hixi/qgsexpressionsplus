from qgis.core import *
from qgis.utils import *


def get_env_variable(var_name):
    """
        Returns the value of a layer, project or global variable

        <p><h4>Syntax</h4>
        get_env_variable(<i>var_name</i>)</p>

        <p><h4>Arguments</h4>
        <i>  var_name</i> &rarr; the name of the variable whose value is required<br></p>

        <p><h4>Example</h4>
        <!-- Show example of function.-->
             get_env_variable('qgis_release_name') &rarr; 'Las Palmas'</p>
    """
    active_layer = iface.activeLayer()
    value = QgsExpressionContextUtils.layerScope(active_layer).variable(var_name) \
            or QgsExpressionContextUtils.projectScope().variable(var_name) \
            or QgsExpressionContextUtils.globalScope().variable(var_name)
    return str(value)
