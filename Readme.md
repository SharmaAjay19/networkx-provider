## Networkx Provider
Service to use networkx algorithms for finding optimal node positions in a graph

To deploy to app service windows
1. Create App Service.
2. Add app setting - WEBSITES_PORT = 5555
3. Add site extension python364x64
4. Deploy the code to wwwroot directory
5. From wwwroot directory, run command `D:\home\python364x64\pip.bat install -r requirements.txt`