from flask import Flask, render_template, request
from modules import port_scanner, whois_lookup, dns_resolver, vuln_scanner

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    module = request.form.get('module')
    target = request.form.get('target')
    ports_input = request.form.get('ports', '')

    result = ""

    try:
        if module == "port":
            if not ports_input:
                result = "Please provide ports for scanning."
            else:
                ports = list(map(int, ports_input.split(',')))
                result = port_scanner.web_scan(target, ports)

        elif module == "whois":
            result = whois_lookup.web_whois(target)

        elif module == "dns":
            result = dns_resolver.web_dns(target)

        elif module == "vuln":
            result = vuln_scanner.web_scan(target)

        else:
            result = "Invalid module selected."
    except Exception as e:
        result = f"Error occurred: {e}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
