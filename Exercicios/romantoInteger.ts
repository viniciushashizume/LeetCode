function romanToInt(s: string): number {
    const romanMap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    };
    let resultado: number = 0;
    const tamanho: number = s.length;
    for(let i = 0; i<s.length; i++)
    {
        let valorAtual = romanMap[s[i]];
        let proximoValor = romanMap[s[i+1]];
        if (proximoValor > valorAtual)
        {
            resultado -= valorAtual;
        } 
        else
        {
            resultado += valorAtual;
        }
    }
    return resultado;
};