import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SwitchListComponent } from './switch-list.component';

describe('SwitchListComponent', () => {
  let component: SwitchListComponent;
  let fixture: ComponentFixture<SwitchListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SwitchListComponent]
    });
    fixture = TestBed.createComponent(SwitchListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
