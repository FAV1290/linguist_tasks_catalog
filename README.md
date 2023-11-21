<div width='100%' align='center'>
    <h1><img src='readme_assets\title.png' height='64'/> (Linguist tasks catalog)</h1> 
    <table border='0'>
        <tr>
            <td><img src='readme_assets\cat1.png' height='256'/></td>
            <td>
                <p><h2>What is TaskCat?</h2></p>
                <br>
                A Small Flask webapp for AVT linguists, which helps:
                <li>Control assigned tasks status</li>
                <li>Calculate estimated salary for period</li>
                <li>Customize clients, task types and pricing schemes for them</li>  
            </td>
        </tr>
        <tr>
            <td align='center'>
                <p><h2>Requirements</h2></p>
                <br>
                <p><a href='requirements.txt'>Here they are...</a></p>
            </td>
            <td align='center'>
                <img src='readme_assets\cat2.png' height='256'/>
            </td>
        </tr>
        <tr>
            <td>
                <img src='readme_assets\cat3.png' height='256'/>
            </td>
            <td>
                <p><h2>Project setup</h2></p>
                <br>
                <li>Clone repo: <code>git clone https://github.com/FAV1290/linguist_tasks_catalog/</code></li>
                <li>Open repo catalog: <code>cd linguist_tasks_catalog</code>
                <li>Install requirements: <code>pip install -r requirements.txt</code></li>
                <li>Add environment variable or .env <code>TASKCAT_SECRET_KEY</code> with code phrase you like</li>
                <li>Add environment variable or .env <code>TASKCAT_DB_HOST</code> with postgresql-link to db</li>
                <li>Initialize database models: <code>python -m db.models</li></code>
                <li>Run development server: <code>python main.py</li></code></li>
            </td>
        </tr>
    </table>
    <h1>How does it look?</h1>
    <br>
    <img src='readme_assets\screenshot1.png'/>
    <img src='readme_assets\screenshot2.png'/>
    <img src='readme_assets\screenshot3.png'/>
</div>
