// https://source.sae-suki-blog.net/conoha-to-weblog/csv-to-table-javascript/
window.addEventListener('load', async () => {
    
    const csv2tableClass = document.getElementsByClassName('csv2table');
    
    const elements = Array.from(csv2tableClass);
    
    for (let n = 0; n < elements.length; n++) {
        // csv読み込み //////////
        const src = elements[n].getAttribute('data-src');
        const text = await (await fetch(src)).text();
        
        // セル分割 //////////
        const cells = CSV.parse(text);
        
        // ラベル読み込み //////////
        const label = elements[n].getAttribute('data-label');
        
        // テーブル作成 //////////
        let output = '';
        if (elements[n].hasAttribute('data-label')) {
            output += '<table class="csv2table ' + label + '">';
        }
        else {
            output += '<table class="csv2table">';
        }
        
        // ヘッダー部 ----------
        output += '<thead>';
        {
            output += '<tr>';
            for (let j = 0; j < cells[0].length; j++) {
                output += '<th>' + cells[0][j] + '</th>';
            }
            output += '</tr>';
        }
        output += '</thead>';
        
        // ボディー部 ----------
        output += '<tbody>';
        for (let i = 1; i < cells.length; i++) {
            output += '<tr>';
            for (let j = 0; j < cells[i].length; j++) {
                output += '<td>' + cells[i][j] + '</td>';
            }
            output += '</tr>';
        }
        output += '</tbody>';
        
        // テーブル作成終了 //////////
        output += '</table>';
        
        // htmlへ出力 //////////
        elements[n].innerHTML = output;
    }
    
}, false);