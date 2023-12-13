import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import * as fg from 'force-graph';

@Component({
  selector: 'app-topology-graph',
  templateUrl: './topology-graph.component.html',
  styleUrls: ['./topology-graph.component.scss']
})
export class TopologyGraphComponent implements OnInit {
  @ViewChild('graph') graph: ElementRef;
  data:any = {
    "nodes": [
        {"id": "1",  "val": 2, "color":"rgb(255,0,0,0.8)"},
        {"id": "2",  "val": 2, "color":"rgb(0,255,0,0.8)"},
        {"id": "3",  "val": 2, "color":"rgb(0,0,255,0.8)"},
        {"id": "4",  "val": 2, "color":"rgb(255,0,0,0.8)"},
        {"id": "5",  "val": 3, "color":"rgb(255,0,0,0.8)"},
        {"id": "6",  "val": 4, "color":"rgb(255,0,0,0.8)"},
        {"id": "7",  "val": 2, "color":"rgb(255,0,0,0.8)"},
        {"id": "8",  "val": 4, "color":"rgb(255,0,0,0.8)"},
        {"id": "9",  "val": 2, "color":"rgb(255,0,0,0.8)"},
        {"id": "10",  "val": 3, "color":"rgb(255,0,0,0.8)"}
    ],
    "links": [
        {"source": "1", "target":"2"},
        {"source": "1", "target":"3"},
        {"source": "1", "target":"4"},
        {"source": "1", "target":"5"},
        {"source": "1", "target":"6"},
        {"source": "1", "target":"7"},
        {"source": "1", "target":"8"},
        {"source": "1", "target":"9"},
        {"source": "1", "target":"10"},
        {"source": "2", "target":"3"},
        {"source": "2", "target":"4"},
        {"source": "2", "target":"5"},
        {"source": "2", "target":"6"},
        {"source": "2", "target":"9"},
        {"source": "2", "target":"10"},
        {"source": "3", "target":"7"},
        {"source": "3", "target":"8"},
        {"source": "3", "target":"9"},
        {"source": "3", "target":"10"},
        {"source": "4", "target":"5"},
        {"source": "4", "target":"6"},
        {"source": "4", "target":"7"},
        {"source": "5", "target":"6"},
        {"source": "5", "target":"7"},
        {"source": "5", "target":"8"},
        {"source": "6", "target":"9"},
        {"source": "6", "target":"10"},
        {"source": "7", "target":"8"},
        {"source": "7", "target":"9"},
        {"source": "7", "target":"10"},
        {"source": "8", "target":"9"},
        {"source": "8", "target":"10"},
        {"source": "9", "target":"10"}
    ]
    
}
  ngOnInit(): void {
    
  }
  ngAfterViewInit() {
    // Şimdi burada div'in genişliğini alabilirsiniz.
    const divWidth = this.graph.nativeElement.offsetWidth;
    const divHeieght = this.graph.nativeElement.offsetHeight;
    console.log('Div Genişliği:', divWidth);

      const graph = fg.default()
        (document.getElementById('graph'))
        .backgroundColor('#101020')
        .width(divWidth)
        .height(divHeieght)
        .linkColor(link => link.source == "1" && link.target == "2" ? 'rgb(255,0,0,0.8)' : 'rgb(0,255,0,0.8)')
        .nodeAutoColorBy('color')
        .nodeVal('val')
        .nodeLabel('id')
        .linkDirectionalParticles(1)
        .graphData(this.data)
  }
}