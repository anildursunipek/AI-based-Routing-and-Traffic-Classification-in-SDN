import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrafficGenerateComponent } from './traffic-generate.component';

describe('TrafficGenerateComponent', () => {
  let component: TrafficGenerateComponent;
  let fixture: ComponentFixture<TrafficGenerateComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TrafficGenerateComponent]
    });
    fixture = TestBed.createComponent(TrafficGenerateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
