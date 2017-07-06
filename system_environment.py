from qgis.core import qgsfunction
import qgis


@qgsfunction(1, "Expressions +", register=False)
def env(var_name, *args):
    """
        Returns the value of a system variable. If it isn't available, returns an empty string.

        <p><h4>Syntax</h4>
        env(<i>var_name</i>)</p>

        <p><h4>Arguments</h4>
        <i>  var_name</i> &rarr; the name of the variable whose value is required<br></p>

        <p><h4>Example</h4>
        <!-- Show example of function.-->
             env('USER') &rarr; 'ExampleUser'</p>
    """
    return qgis.user.os.getenv(var_name, '')
