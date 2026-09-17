import http from 'k6/http';
import { sleep, check } from 'k6';

export default function () {
    let res = http.get('http://localhost:8501');
    check(res, {
        'HUD is active (status 200)': (r) => r.status === 200,
    });
    sleep(1);
}
