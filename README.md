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
            <td>
                <p><h2>Requirements</h2></p>
                <br>
                <details>
                    <summary>Here they are...</summary>
                    <br>
                    <li>blinker==1.6.3</li>
                    <li>certifi==2023.7.22</li>
                    <li>charset-normalizer==3.3.2</li>
                    <li>click==8.1.7</li>
                    <li>colorama==0.4.6</li>
                    <li>flake8==6.1.0</li>
                    <li>Flask==3.0.0</li>
                    <li>Flask-Login==0.6.3</li>
                    <li>Flask-WTF==1.2.1</li>
                    <li>greenlet==3.0.1</li>
                    <li>idna==3.4</li>
                    <li>iniconfig==2.0.0</li>
                    <li>itsdangerous==2.1.2</li>
                    <li>Jinja2==3.1.2</li>
                    <li>MarkupSafe==2.1.3</li>
                    <li>mccabe==0.7.0</li>
                    <li>mypy==1.6.1</li>
                    <li>mypy-extensions==1.0.0</li>
                    <li>packaging==23.2</li>
                    <li>pluggy==1.3.0</li>
                    <li>psycopg2==2.9.9</li>
                    <li>pycodestyle==2.11.1</li>
                    <li>pyflakes==3.1.0</li>
                    <li>pytest==7.4.3</li>
                    <li>python-dotenv==1.0.0</li>
                    <li>requests==2.31.0</li>
                    <li>SQLAlchemy==2.0.22</li>
                    <li>typing_extensions==4.8.0</li>
                    <li>urllib3==2.0.7</li>
                    <li>Werkzeug==3.0.1</li>
                    <li>WTForms==3.1.1</li>
                </details>
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
</div>
