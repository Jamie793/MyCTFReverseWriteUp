#include <iostream>
using namespace std;

void decrypt(uint32_t *v, uint32_t *k)
{
    uint32_t v0 = v[0], v1 = v[1], sum = 0x458BCD42 * 64, i;  /* set up */
    uint32_t delta = 0x458BCD42;                         /* a key schedule constant */
    uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3]; /* cache key */
    for (i = 0; i < 32; i++)
    { /* basic cycle start */
        v1 -= ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3);
        v0 -= ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1);
        sum -= delta;
    } /* end cycle */
    v[0] = v0;
    v[1] = v1;
}

int mian()
{
    unsigned int encData[6];
    encData[2] = 3774025685;
    encData[3] = 1548802262;
    encData[4] = 2652626477;
    encData[5] = 2230518816;
    encData[1] = 550153460;
    encData[0] = 374609907;
    unsigned int key[4] = {2, 2, 3, 4};
    for (size_t i = 0; i < 3; i = i + 2)
    {
        decrypt((uint32_t *)&encData[i],(uint32_t *)&key);
    }

    return 0;
}