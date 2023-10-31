import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LinkListComponent } from './link-list.component';

describe('LinkListComponent', () => {
  let component: LinkListComponent;
  let fixture: ComponentFixture<LinkListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LinkListComponent]
    });
    fixture = TestBed.createComponent(LinkListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
