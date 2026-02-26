def test_elastalert2_installed(host):
    cmd = host.run("elastalert --help")
    assert cmd.rc == 0


def test_elastalert_user_exists(host):
    user = host.user("elastalert")
    assert user.exists
    assert user.shell == "/usr/sbin/nologin"


def test_config_directory_exists(host):
    d = host.file("/etc/elastalert2")
    assert d.exists
    assert d.is_directory
    assert d.user == "elastalert"
    assert d.group == "elastalert"
    assert d.mode == 0o750


def test_config_file_exists(host):
    f = host.file("/etc/elastalert2/config.yaml")
    assert f.exists
    assert f.is_file
    assert f.user == "elastalert"
    assert f.group == "elastalert"
    assert f.mode == 0o640


def test_config_contains_es_host(host):
    f = host.file("/etc/elastalert2/config.yaml")
    assert f.contains("es_host: elasticsearch-test")
    assert f.contains("es_port: 9200")


def test_rules_directory_exists(host):
    d = host.file("/etc/elastalert2/rules")
    assert d.exists
    assert d.is_directory
    assert d.user == "elastalert"
    assert d.group == "elastalert"
    assert d.mode == 0o750


def test_rule_file_exists(host):
    f = host.file("/etc/elastalert2/rules/test_rule.yaml")
    assert f.exists
    assert f.is_file
    assert f.user == "elastalert"
    assert f.group == "elastalert"
    assert f.mode == 0o640
    assert f.contains("name: Test rule")
    assert f.contains("type: any")


def test_systemd_unit_exists(host):
    f = host.file("/etc/systemd/system/elastalert2.service")
    assert f.exists
    assert f.is_file
    assert f.contains("ExecStart=/usr/local/bin/elastalert")


def test_service_enabled_and_running(host):
    service = host.service("elastalert2")
    assert service.is_enabled
    assert service.is_running


def test_writeback_index_created(host):
    cmd = host.run(
        "python3 -c \""
        "import urllib.request; "
        "r = urllib.request.urlopen('http://elasticsearch-test:9200/elastalert_status'); "
        "print(r.status)\""
    )
    assert cmd.stdout.strip() == "200"
