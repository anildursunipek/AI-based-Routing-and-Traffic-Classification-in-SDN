import { TestBed } from '@angular/core/testing';

import { SingleSwitchService } from './single-switch.service';

describe('SingleSwitchService', () => {
  let service: SingleSwitchService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SingleSwitchService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
