import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TopologyGraphComponent } from './topology-graph.component';

describe('TopologyGraphComponent', () => {
  let component: TopologyGraphComponent;
  let fixture: ComponentFixture<TopologyGraphComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TopologyGraphComponent]
    });
    fixture = TestBed.createComponent(TopologyGraphComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
