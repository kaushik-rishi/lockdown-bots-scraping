#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define int long long
#define endl "\n"
#define all(x) x.begin(), x.end()
#define deb(x) cout << #x << " --> " << (x) << endl
#define pb push_back
#define mod 1000000007  // 1e9 + 7
#define prec(x, y) fixed << setprecision(y) << x
#define print(v)                       \
    for (auto x : v) cout << x << " "; \
    cout << endl

void solve() {
    int i, j, n, k;
    cin >> n;
    string s;
    cin >> s;
    int cntopen = 0, cntclose = 0;
    vector<pair<int, int>> v(s.size());
    int ans = INT_MIN;
    for (i = 0; i < s.size(); ++i) {
        if (s[i] == '(') cntopen++;
        if (s[i] == ')') cntclose++;
        ans = max((cntclose - cntopen), ans);
    }
    cout << ans << endl;
}

//Fuck Ratings
//Once a Charas always a Charas

int32_t main() {
    ios::sync_with_stdio(0);
    cout.tie(0);
    cin.tie(0);
    int _t = 1;
    cin >> _t;
    while (_t--)
        solve();
}