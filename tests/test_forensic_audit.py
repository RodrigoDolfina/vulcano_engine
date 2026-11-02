import os
import gzip

def test_forensic_log_compression(tmp_path):
    log_file = tmp_path / 'audit_security.log'
    log_file.write_text('2026-11-01 10:10:00 [SECURITY] HMAC Validation Success - EventID: 9942')
    gz_file = tmp_path / 'audit_security.log.gz'
    with open(log_file, 'rb') as f_in:
        with gzip.open(gz_file, 'wb') as f_out:
            f_out.writelines(f_in)
    assert os.path.exists(gz_file)
    with gzip.open(gz_file, 'rt') as f_in:
        content = f_in.read()
        assert 'HMAC Validation Success' in content
